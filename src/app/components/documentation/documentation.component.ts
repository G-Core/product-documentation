import { ViewportScroller } from '@angular/common';
import {
    AfterViewChecked,
    ChangeDetectorRef,
    Component,
    ElementRef,
    NgZone,
    OnDestroy,
    OnInit,
    Renderer2,
    ViewChild,
    ViewEncapsulation,
} from '@angular/core';
import { ActivatedRoute, NavigationEnd, Router } from '@angular/router';
import { isScullyRunning, ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { combineLatest, first, map, Observable, of, Subscription, take } from 'rxjs';
import { categories, DOCS_GITHUB_REPO, HEADER_HEIGHT, METADATA_FILE_TITLE } from '../../constants';
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
    public activeMenuItem: MenuItem;
    public activeUrl: string;
    public showContent: boolean;
    public breadCrumbs: Array<MenuItem> = [];
    public githubUrl: string;
    public lastModifiedLabel: string = '';
    public tableOfContents: Array<TableOfContents> = [];
    public tableOfContentsHeaders: Array<Element> = [];
    public activeTocItem: string = '';
    public showFullSizeImage: boolean = false;
    public targetImageSrc: string = '';
    public isMenuExpanded: boolean = false;
    public category: string;
    public callToActionMap = callToActionMap;
    public isActiveLike: boolean = false;
    public isActiveDislike: boolean = false;
    public activeTab: string;
    public baseHref: string = environment.baseHref;
    public isArticleRated: boolean = false;
    public isEditArticleGuidePage: boolean = false;

    private routerSubscription: Subscription;

    @ViewChild('scullyContainer') public scullyContainer: ElementRef;
    @ViewChild('fullSizeImage') public fullSizeImage: ElementRef;

    constructor(
        private scully: ScullyRoutesService,
        private router: Router,
        private route: ActivatedRoute,
        private githubApiService: GitHubAPIService,
        private viewportScroller: ViewportScroller,
        private ngZone: NgZone,
        private renderer: Renderer2,
        private changeDetectorRef: ChangeDetectorRef,
        private data: MenuService,
    ) {}

    public ngAfterViewChecked(): void {
        this.route.fragment.pipe(first()).subscribe((fragment) => {
            this.viewportScroller.scrollToAnchor(fragment);
        });

        if (this.scullyContainer.nativeElement) {
            this.scullyContainer.nativeElement.querySelectorAll(':not(.gc-gallery p) > img').forEach((img: Element) => {
                this.ngZone.runOutsideAngular(() => {
                    this.renderer.listen(img, 'click', (event) => this.expandImage(event));
                });
            });

            this.ngZone.runOutsideAngular(() => {
                window.document.addEventListener('scroll', this.handlePageScroll, true);
            });

            this.ngZone.runOutsideAngular(() => {
                this.renderer.listen(this.fullSizeImage.nativeElement, 'click', () => this.closeFullSizeModal());
            });

            if (this.tableOfContents) {
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
    }

    public getAnchor(anchorIndex: number, pageUrl: string): string {
        return anchorIndex !== -1 ? (pageUrl = pageUrl.slice(0, anchorIndex)) : pageUrl;
    }

    public setBreadCrumbs(pageUrl: string, category: string): Array<MenuItem> {
        const breadcrumbs = [
            {
                name: this.activeMenuItem.name,
                url: `/${category}`,
            },
        ];

        if (!pageUrl.includes('/reseller-support')) {
            breadcrumbs.unshift({
                name: 'Home',
                url: '/',
            });
        }
        return breadcrumbs;
    }

    public ngOnInit(): void {
        this.data.toggleMenuEmitted$.subscribe(() => {
            this.isMenuExpanded = !this.isMenuExpanded;
            this.changeDetectorRef.detectChanges();
        });

        this.links$ = combineLatest([this.route.url, this.scully.available$]).pipe(
            map(([url, links]) => {
                const anchorIndex = this.router.url.indexOf('#');
                let pageUrl = this.router.url;

                pageUrl = this.getAnchor(anchorIndex, pageUrl);

                const documentUrlWithCategory = pageUrl.replace('/', '');
                const category = url[0].path;
                this.category = category;
                const documentUrl = documentUrlWithCategory.replace(category, '').slice(1);
                const document = documentUrl.length ? documentUrl.slice(documentUrl.lastIndexOf('/') + 1) : '';

                this.activeUrl = pageUrl;
                this.activeMenuItem = {
                    name: categories.find((categoryItem) => categoryItem.url === category)?.name,
                    url: category,
                };
                this.showContent = !!document;
                this.tableOfContents = [];

                this.isEditArticleGuidePage = category === 'edit-article-guide' ? true : false;

                const filterdLinks = links.filter(({ route }) => {
                    return route.replace('/', '').startsWith(category) && !route.endsWith(`/${category}`);
                });

                this.setTableOfContent(filterdLinks);

                const breadcrumbs = this.setBreadCrumbs(pageUrl, category);

                if (this.showContent) {
                    this.githubUrl = `${DOCS_GITHUB_REPO}${documentUrlWithCategory}.md`;
                    if (!isScullyRunning()) {
                        this.setLastModifiedDate(`documentation/${documentUrlWithCategory}.md`);
                    }
                    documentUrl
                        .split('/')
                        .filter((value) => value)
                        .forEach((routeSegment, index, arr) => {
                            breadcrumbs.push({
                                name:
                                    index === arr.length - 1
                                        ? filterdLinks.find((link) => link.title === document)?.displayName
                                        : filterdLinks.find(
                                              (link) =>
                                                  link.title === METADATA_FILE_TITLE &&
                                                  link.route.endsWith(`${routeSegment}/metadata`),
                                          )?.displayName || routeSegment.split('-').join(' '),
                                url: '',
                            });
                        });
                }

                this.breadCrumbs = breadcrumbs;

                const menuTree = new Map<string, MenuTreeItem>();

                filterdLinks.forEach((link) => {
                    const routeSegments = link.route.replace(`/${category}/`, '').split('/');

                    if (routeSegments.length === 1) {
                        menuTree.set(routeSegments[0], {
                            url: link.redirect || link.route,
                            name: link.displayName,
                            order: link.order,
                            title: link.title,
                            children: null,
                        });
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

    private setTableOfContent(links: Array<ScullyRoute>): void {
        const currentLink = links.find(({ route }) => route === this.activeUrl);
        if (currentLink && currentLink.toc) {
            this.tableOfContents = Object.keys(currentLink.toc).map((key) => ({
                lvl: this.getContentLevel(key),
                name: key.replace(/--\d--/g, ''),
                fragment: currentLink.toc[key],
            }));
        }
    }

    // Recursively build menu tree
    private buildMenuSubTree(tree: Map<string, MenuTreeItem>, routeSegments: Array<string>, link: ScullyRoute): void {
        const unhandledRouteSegments = routeSegments.slice(1);
        let menuItem;
        if (tree.has(routeSegments[0])) {
            menuItem = tree.get(routeSegments[0]);
            if (!menuItem.children) {
                menuItem.children = new Map();
            }
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
            if (document.documentElement.scrollTop + HEADER_HEIGHT + 18 > (item as HTMLElement).offsetTop) {
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

    private getContentLevel(name: string): number {
        const regExp = /--\d--/i;
        if (regExp.test(name)) {
            return +name.slice(0, 4).replace(/-/g, '');
        }
        return 1;
    }
}
