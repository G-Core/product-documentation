import { ViewportScroller } from '@angular/common';
import {
  AfterViewChecked,
  ChangeDetectorRef,
  Component,
  ElementRef,
  NgZone,
  OnInit,
  ViewChild,
  ViewEncapsulation,
} from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { combineLatest, first, map, Observable, of, take } from 'rxjs';
import {
  categories,
  DOCS_GITHUB_REPO,
  HEADER_HEIGHT,
  METADATA_FILE_TITLE,
} from '../../constants';
import { MenuItem, MenuTreeItem, TableOfContents } from '../../models';
import { GitHubAPIService } from '../../services';

@Component({
  selector: 'gc-documentation',
  templateUrl: './documentation.component.html',
  preserveWhitespaces: true,
  styleUrls: ['./documentation.component.scss'],
  encapsulation: ViewEncapsulation.Emulated,
})
export class DocumentationComponent implements OnInit, AfterViewChecked {
  links$: Observable<MenuItem[]> = of([]);
  activeMenuItem: MenuItem;
  activeUrl: string;
  showContent: boolean;
  breadCrumbs: MenuItem[] = [];
  githubUrl: string;
  lastModifiedLabel: string = '';
  tableOfContents: TableOfContents[] = [];
  tableOfContentsHeaders: Element[] = [];
  activeTocItem: string = '';
  showFullSizeImage: boolean = false;
  targetImageSrc: string = '';

  @ViewChild('scullyContainer') scullyContainer: ElementRef;

  constructor(
    private scully: ScullyRoutesService,
    private router: Router,
    private route: ActivatedRoute,
    private githubApiService: GitHubAPIService,
    private viewportScroller: ViewportScroller,
    private ngZone: NgZone,
    private changeDetectorRef: ChangeDetectorRef
  ) {}

  ngAfterViewChecked(): void {
    this.route.fragment.pipe(first()).subscribe((fragment) => {
      this.viewportScroller.scrollToAnchor(fragment);
    });
    if (this.scullyContainer.nativeElement) {
      this.scullyContainer.nativeElement
        .querySelectorAll(':not(.gc-gallery p) > img')
        .forEach((img: Element) =>
          img.addEventListener('click', this.expandImage)
        );

      if (this.tableOfContents) {
        this.tableOfContentsHeaders = this.tableOfContents
          .map((contentItem: any) =>
            document.querySelector('#' + contentItem.fragment)
          )
          .filter((item: Element) => item);
      }
      this.ngZone.runOutsideAngular(() => {
        window.document.addEventListener('scroll', this.handlePageScroll, true);
      });

      this.handlePageScroll();
    }
  }

  ngOnInit(): void {
    this.links$ = combineLatest([this.route.url, this.scully.available$]).pipe(
      map(([url, links]) => {
        const anchorIndex = this.router.url.indexOf('#');
        let pageUrl = this.router.url;
        if (anchorIndex !== -1) {
          pageUrl = pageUrl.slice(0, anchorIndex);
        }

        const documentUrlWithCategory = pageUrl.replace('/documentation/', '');
        const category = url[1].path;
        let documentUrl = documentUrlWithCategory
          .replace(category, '')
          .slice(1);
        const document = documentUrl.length
          ? documentUrl.slice(documentUrl.lastIndexOf('/') + 1)
          : '';

        this.activeUrl = pageUrl;
        this.activeMenuItem = {
          name: categories.find((categoryItem) => categoryItem.url === category)
            ?.name,
          url: category,
        };
        this.showContent = !!document;
        this.tableOfContents = [];

        const filterdLinks = links.filter(({ route, toc }) => {
          if (route === pageUrl && toc) {
            this.tableOfContents = Object.keys(toc).map((key) => ({
              lvl: this.getContentLevel(key),
              name: key.replace(/--\d--/g, ''),
              fragment: toc[key],
            }));
          }
          return route.includes(category) && !route.endsWith(category);
        });

        const breadcrumbs = [
          {
            name: 'Home',
            url: '/',
          },
          {
            name: this.activeMenuItem.name,
            url: `/documentation/${category}`,
          },
        ];

        if (this.showContent) {
          this.githubUrl = `${DOCS_GITHUB_REPO}${documentUrl}.md`;
          this.setLastModifiedDate(`documentation/${documentUrl}`);
          documentUrl
            .split('/')
            .filter((value) => value)
            .forEach((routeSegment, index, arr) => {
              breadcrumbs.push({
                name:
                  index === arr.length - 1
                    ? filterdLinks.find((link) => link.title === document)
                        ?.displayName
                    : routeSegment.split('-').join(' '),
                url: '',
              });
            });
        }

        this.breadCrumbs = breadcrumbs;

        const menuTree = new Map<string, MenuTreeItem>();

        filterdLinks.forEach((link) => {
          const routeSegments = link.route
            .replace(`/documentation/${category}/`, '')
            .split('/');

          if (routeSegments.length === 1) {
            menuTree.set(routeSegments[0], {
              url: link.route,
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
      })
    );
  }

  closeFullSizeModal() {
    this.showFullSizeImage = false;
    this.targetImageSrc = '';
  }

  // Recursively build menu tree
  private buildMenuSubTree(
    tree: Map<string, MenuTreeItem>,
    routeSegments: string[],
    link: ScullyRoute
  ): void {
    const unhandledRouteSegments = routeSegments.slice(1);
    let menuItem;
    if (tree.has(routeSegments[0])) {
      menuItem = tree.get(routeSegments[0]);
      if (!menuItem.children) {
        menuItem.children = new Map();
      }
    } else {
      menuItem = {
        url: unhandledRouteSegments.length ? '' : link.route,
        order: unhandledRouteSegments.length ? 0 : link.order,
        title: unhandledRouteSegments.length ? '' : link.title,
        name: unhandledRouteSegments.length
          ? routeSegments[0]
          : link.displayName,
        children: new Map(),
      };
      tree.set(routeSegments[0], menuItem);
    }

    if (unhandledRouteSegments.length) {
      this.buildMenuSubTree(menuItem.children, unhandledRouteSegments, link);
    }
  }

  private expandImage = (event: Event) => {
    const targetImage = event.target as HTMLElement;
    this.showFullSizeImage = true;
    this.targetImageSrc = targetImage.getAttribute('src');
  };

  private handlePageScroll = () => {
    const activeSectionId = this.tableOfContentsHeaders.reduce(
      (activeItem: string, item) => {
        if (
          document.documentElement.scrollTop + HEADER_HEIGHT + 18 >
          (item as HTMLElement).offsetTop
        ) {
          activeItem = item.id;
        }
        return activeItem;
      },
      this.tableOfContentsHeaders[0]?.id
    );
    if (this.activeTocItem !== activeSectionId) {
      this.activeTocItem = activeSectionId;
      this.changeDetectorRef.detectChanges();
    }
  };

  private convertToArray(menuMap: Map<string, MenuTreeItem>): MenuItem[] {
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
        }
        return menuItem;
      })
      .sort((a, b) => {
        const aOrder = a.order || this.getFolderMetadataOrder(a) || 9999;
        const bOrder = b.order || this.getFolderMetadataOrder(b) || 9999;
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

  private getFolderMetadataOrder(menuItem: MenuItem): number {
    if (!menuItem || !menuItem.children || !menuItem.children.length) {
      return 9999;
    }
    const metadataDoc = menuItem.children.find(
      (item) => item.title === METADATA_FILE_TITLE
    );

    // Set order to folder menu item
    if (metadataDoc) {
      menuItem.order = metadataDoc.order;
      return metadataDoc.order;
    }

    return 9999;
  }

  private getContentLevel(name: string): number {
    const regExp = /--\d--/i;
    if (regExp.test(name)) {
      return +name.slice(0, 4).replace(/-/g, '');
    }
    return 1;
  }
}
