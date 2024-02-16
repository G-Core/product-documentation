import { ViewportScroller } from '@angular/common';
import {
    AfterViewChecked,
    ChangeDetectorRef,
    Component,
    ElementRef,
    OnDestroy,
    OnInit,
    Renderer2,
    ViewChild,
    ViewEncapsulation,
} from '@angular/core';
import { ActivatedRoute, NavigationEnd, Router } from '@angular/router';
import { isScullyRunning, ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { combineLatest, first, map, Observable, of, Subscription, take } from 'rxjs';
import { categories, HEADER_HEIGHT, headerTagNameList, METADATA_FILE_TITLE } from '../../constants';
import { MenuItem, MenuTreeItem, TableOfContents } from '../../models';
import { GitHubAPIService } from '../../services';
import { MenuService } from '../../services/menu.service';
import { callToActionMap } from '../../constants/call-to-action';
import { environment } from '../../../environments/environment';

@Component({
    selector: 'gc-documentation',
    templateUrl: './documentation.component.html',
    preserveWhitespaces: true,
    styleUrls: ['./documentation.component.scss'],
    encapsulation: ViewEncapsulation.Emulated,
})
export class DocumentationComponent implements OnInit, AfterViewChecked, OnDestroy {
    public links$: Observable<Array<MenuItem>> = of([]);
    public activeCategoryItem: MenuItem;
    public activeUrl: string;
    public showContent: boolean;
    public breadCrumbs: Array<MenuItem> = [];
    public githubUrl: string;
    public lastModifiedLabel: string = '';
    public tableOfContents: Array<TableOfContents> = [];
    public tableOfContentsHeaders: Array<Element> = [];
    public activeTocItem: string = '';
    public targetImageSrc: string = '';
    public isMenuExpanded: boolean = false;
    public category: string;
    public callToActionMap = callToActionMap;
    public isActiveLike: boolean = false;
    public isActiveDislike: boolean = false;
    public activeTab: string;
    public baseHref: string = environment.baseHref;
    public isArticleRated: boolean = false;
    public isArticleReady: boolean = false;
    public isEditArticleGuidePage: boolean = false;
    public activeDocument: ScullyRoute;

    private routerSubscription: Subscription;
    private hasScrolled = false;
    public isResellerPage = false;

    @ViewChild('scullyContainer') public scullyContainer: ElementRef;
    @ViewChild('fullSizeImage') public fullSizeImage: ElementRef;

    constructor(
        private scully: ScullyRoutesService,
        private router: Router,
        private route: ActivatedRoute,
        private githubApiService: GitHubAPIService,
        private viewportScroller: ViewportScroller,
        private renderer: Renderer2,
        private changeDetectorRef: ChangeDetectorRef,
        private data: MenuService,
    ) {}

    public ngAfterViewChecked(): void {
        if (this.scullyContainer.nativeElement) {
            if (this.scullyContainer.nativeElement.childElementCount > 1) {
                this.isArticleReady = true;
                this.changeDetectorRef.detectChanges();
            } else {
                this.isArticleReady = false;
                this.changeDetectorRef.detectChanges();
            }

            if (this.isArticleReady && !this.hasScrolled) {
                this.route.fragment.pipe(first()).subscribe((fragment) => {
                    this.viewportScroller.scrollToAnchor(fragment);
                    this.hasScrolled = true;
                });

                this.scullyContainer.nativeElement
                    .querySelectorAll(':not(.gc-gallery p) > img')
                    .forEach((img: Element) => {
                        this.renderer.listen(img, 'click', (event) => this.expandImage(event));
                    });

                window.document.addEventListener('scroll', this.handlePageScroll, true);

                this.renderer.listen(this.fullSizeImage.nativeElement, 'click', () => this.closeFullSizeModal());
            }
        }

        if (this.isArticleReady && this.tableOfContents) {
            this.tableOfContentsHeaders = this.tableOfContents
                .map(({ fragment }) => {
                    if (fragment) {
                        return document.getElementById(`${fragment}`);
                    }
                    return null;
                })
                .filter((item: Element) => item);
        }
    }

    public ngOnInit(): void {
        this.data.toggleMenuEmitted$.subscribe(() => {
            this.isMenuExpanded = !this.isMenuExpanded;
            this.changeDetectorRef.detectChanges();
        });

        this.isResellerPage = this.router.url.includes('reseller-support');

        this.links$ = combineLatest([this.route.url, this.scully.available$]).pipe(
            map(([url, links]) => {
                const anchorIndex = this.router.url.indexOf('#');
                const pageUrl = this.getAnchor(anchorIndex, this.router.url);
                this.category = url[0].path;
                this.activeUrl = pageUrl;
                this.activeCategoryItem = {
                    name: categories.find((categoryItem) => categoryItem.url === this.category)?.name,
                    url: this.category,
                };

                const filteredByCategoryLinks = links.filter(({ route }) => {
                    return route.replace('/', '').startsWith(this.category) && !route.endsWith(`/${this.category}`);
                });

                this.activeDocument = filteredByCategoryLinks.find(
                    (link) => link.route === pageUrl || link.originalUrl === pageUrl,
                );

                const documentUrlWithCategory = (this.activeDocument?.originalUrl || pageUrl).replace('/', '');
                const documentUrl = documentUrlWithCategory.replace(this.category, '').slice(1);
                const document = documentUrl.length ? documentUrl.slice(documentUrl.lastIndexOf('/') + 1) : '';

                this.showContent = !!this.activeDocument;

                this.setTableOfContent(filteredByCategoryLinks);
                this.breadCrumbs = this.getDocumentBreadcrumbs(pageUrl, documentUrl, document, filteredByCategoryLinks);

                if (this.showContent && !isScullyRunning()) {
                    this.setLastModifiedDate(`documentation/${documentUrlWithCategory as string}.md`);
                }

                const menuTree = new Map<string, MenuTreeItem>();

                filteredByCategoryLinks.forEach((link) => {
                    const routeSegments = (link.originalUrl || link.route).replace(`/${this.category}/`, '').split('/');

                    if (routeSegments.length === 1) {
                        if (menuTree.has(routeSegments[0])) {
                            menuTree.get(routeSegments[0]).url = link.route;
                        } else {
                            menuTree.set(routeSegments[0], {
                                url: link.redirect || link.route,
                                name: link.displayName,
                                order: link.order,
                                title: link.title,
                                children: null,
                            });
                        }
                    } else {
                        this.buildMenuSubTree(menuTree, routeSegments, link);
                    }
                });

                return this.convertToArray(menuTree);
            }),
        );

        this.routerSubscription = this.router.events.subscribe((event) => {
            if (event instanceof NavigationEnd) {
                this.isArticleRated = false;
                this.isActiveLike = false;
                this.isActiveDislike = false;
                this.isResellerPage = this.router.url.includes('reseller-support');
                this.changeDetectorRef.detectChanges();
            }
        });
    }

    public ngOnDestroy(): void {
        if (this.routerSubscription) {
            this.routerSubscription.unsubscribe();
        }
    }

    public anchorScroll(hash: string): void {
        document.location.hash = hash;
        this.activeTocItem = hash;
        this.activeTab = hash;
        this.changeDetectorRef.detectChanges();
    }

    public closeFullSizeModal(): void {
        this.renderer.removeClass(this.fullSizeImage.nativeElement, 'active');
        this.targetImageSrc = '';
        this.changeDetectorRef.detectChanges();
    }

    public onButtonLikeClick(): void {
        this.isActiveLike = !this.isActiveLike;
        this.isActiveDislike = this.isActiveLike ? false : this.isActiveDislike;
        this.onArticleRated();
    }

    public onButtonDislikeClick(): void {
        this.isActiveDislike = !this.isActiveDislike;
        this.isActiveLike = this.isActiveDislike ? false : this.isActiveLike;
        this.onArticleRated();
    }

    public onArticleRated(): void {
        this.isArticleRated = true;
    }

    public setActiveDoc(): void {
        sessionStorage.setItem('activeDocument', this.activeDocument.originalUrl || this.activeDocument.route);
    }

    private setTableOfContent(links: Array<ScullyRoute>): void {
        const currentLink = links.find(({ route }) => route === this.activeUrl);
        if (currentLink && currentLink.toc) {
            this.tableOfContents = Object.keys(currentLink.toc).map((key) => ({
                lvl: this.getContentLevel(key),
                name: key.replace(/--\d--/g, ''),
                fragment: currentLink.toc[key],
            }));
        } else {
            this.tableOfContents = [];
        }
    }

    // Recursively build menu tree
    private buildMenuSubTree(tree: Map<string, MenuTreeItem>, routeSegments: Array<string>, link: ScullyRoute): void {
        const unhandledRouteSegments = routeSegments.slice(1);
        let menuItem;

        if (tree.has(routeSegments[0])) {
            menuItem = tree.get(routeSegments[0]);

            if (!unhandledRouteSegments.length) {
                menuItem.url = link.route;
            }

            menuItem.children = menuItem.children || new Map();
        } else {
            menuItem = {
                url: unhandledRouteSegments.length ? '' : link.redirect || link.route,
                order: unhandledRouteSegments.length ? 0 : link.order,
                title: unhandledRouteSegments.length ? routeSegments[0] : link.title,
                name: unhandledRouteSegments.length ? routeSegments[0] : link.displayName,
                children: new Map(),
            };
            tree.set(routeSegments[0], menuItem);
        }

        if (unhandledRouteSegments.length) {
            this.buildMenuSubTree(menuItem.children, unhandledRouteSegments, link);
        }
    }

    private expandImage(event: Event): void {
        const targetImage = event.target as HTMLElement;
        this.renderer.addClass(this.fullSizeImage.nativeElement, 'active');
        this.targetImageSrc = targetImage.getAttribute('src');
        this.changeDetectorRef.detectChanges();
    }

    private handlePageScroll = (): void => {
        const scrollHeight = document.documentElement.scrollHeight;
        const clientHeight = document.documentElement.clientHeight;
        const height = scrollHeight - clientHeight;
        const scrollTop = document.documentElement.scrollTop + HEADER_HEIGHT + 18;

        if (height <= scrollTop) {
            this.activeTocItem = this.activeTab;
            return;
        }

        const activeSectionId = this.tableOfContentsHeaders.reduce((activeItem: string, item) => {
            if (
                document.documentElement.scrollTop + HEADER_HEIGHT + 18 > (item as HTMLElement).offsetTop &&
                headerTagNameList.includes(item.tagName)
            ) {
                activeItem = item.id;
            }
            return activeItem;
        }, this.tableOfContentsHeaders[0]?.id);
        if (this.activeTocItem !== activeSectionId) {
            this.activeTocItem = activeSectionId;
            this.changeDetectorRef.detectChanges();
        }
    };

    private convertToArray(menuMap: Map<string, MenuTreeItem>): Array<MenuItem> {
        return [...menuMap]
            .map(([_key, value]) => {
                const menuItem: MenuItem = {
                    url: value.url,
                    name: value.name,
                    order: value.order,
                    title: value.title,
                };
                if (value.children && value.children.size) {
                    menuItem.children = this.convertToArray(value.children);
                    this.setFolderMetadata(menuItem);
                }
                return menuItem;
            })
            .sort((a, b) => {
                const aOrder = a.order || 9999;
                const bOrder = b.order || 9999;
                return aOrder - bOrder;
            });
    }

    private setLastModifiedDate(_filePath: string): void {
        this.githubApiService
            .getLastModifiedDateLabel(_filePath)
            .pipe(take(1))
            .subscribe((label) => {
                this.lastModifiedLabel = label;
            });
    }

    private setFolderMetadata(menuItem: MenuItem): void {
        const metadataDoc = menuItem.children.find((item) => item.title === METADATA_FILE_TITLE);

        if (metadataDoc) {
            menuItem.order = metadataDoc.order || 9999;
            menuItem.name = metadataDoc.name || menuItem.name;
        }
    }

    private getAnchor(anchorIndex: number, pageUrl: string): string {
        return anchorIndex !== -1 ? (pageUrl = pageUrl.slice(0, anchorIndex)) : pageUrl;
    }

    private getDocumentBreadcrumbs(
        pageUrl: string,
        documentUrl: string,
        document: string,
        filterdLinks: Array<ScullyRoute>,
    ): Array<MenuItem> {
        const breadcrumbs = [
            {
                name: this.activeCategoryItem.name,
                url: `/${this.category}`,
            },
        ];

        if (!pageUrl.includes('/reseller-support')) {
            breadcrumbs.unshift({
                name: 'Home',
                url: '/',
            });
        }

        if (this.showContent) {
            documentUrl
                .split('/')
                .filter((value) => value)
                .forEach((routeSegment, index, arr) => {
                    const name =
                        index === arr.length - 1
                            ? filterdLinks.find((link) => link.title === document)?.displayName
                            : filterdLinks.find(
                                  (link) =>
                                      link.title === METADATA_FILE_TITLE &&
                                      link.route.endsWith(`${routeSegment}/metadata`),
                              )?.displayName || routeSegment.split('-').join(' ');
                    const url =
                        index === arr.length - 1
                            ? ''
                            : filterdLinks.find((link) => link.title === routeSegment)?.route || '';
                    breadcrumbs.push({
                        name,
                        url,
                    });
                });
        }

        return breadcrumbs;
    }

    private getContentLevel(name: string): number {
        const regExp = /--\d--/i;
        if (regExp.test(name)) {
            return +name.slice(0, 4).replace(/-/g, '');
        }
        return 1;
    }
}
