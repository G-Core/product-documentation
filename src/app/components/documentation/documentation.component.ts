import {
  Component,
  ElementRef,
  OnInit,
  ViewChild,
  ViewEncapsulation,
} from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { combineLatest, map, Observable, of, take } from 'rxjs';
import { categories, DOCS_GITHUB_REPO } from '../../constants';
import { MenuItem, MenuTreeItem } from '../../models';
import { GitHubAPIService } from '../../services';

@Component({
  selector: 'gc-documentation',
  templateUrl: './documentation.component.html',
  preserveWhitespaces: true,
  styleUrls: ['./documentation.component.scss'],
  encapsulation: ViewEncapsulation.Emulated,
})
export class DocumentationComponent implements OnInit {
  links$: Observable<MenuItem[]> = of([]);
  activeMenuItem: MenuItem;
  activeUrl: string;
  showContent: boolean;
  breadCrumbs: MenuItem[] = [];
  githubUrl: string;
  lastModifiedLabel: string = '';
  // tableOfContents: any = [];

  @ViewChild('scullyContainer') scullyContainer: ElementRef;

  constructor(
    private scully: ScullyRoutesService,
    private router: Router,
    private route: ActivatedRoute,
    private githubApiService: GitHubAPIService
  ) {}

  // Table of contents feature
  /* ngAfterViewChecked(): void {
    if (this.scullyContainer.nativeElement) {
      const tableOfContents: any = [];
      this.scullyContainer.nativeElement
        .querySelectorAll('h2')
        ?.forEach((header: HTMLElement) =>
          tableOfContents.push({
            id: header.id,
            name: header.textContent,
          })
        );
      if (
        this.tableOfContents.length !== tableOfContents.length ||
        tableOfContents.some(
          (contentItem: any) =>
            !this.tableOfContents.find(
              (exixtingContentItem: any) =>
                exixtingContentItem.id === contentItem.id
            )
        )
      ) {
        this.tableOfContents = tableOfContents;
      }
    }
  }*/

  ngOnInit(): void {
    this.links$ = combineLatest([this.route.url, this.scully.available$]).pipe(
      map(([url, links]) => {
        const documentUrlWithCategory = this.router.url.replace(
          '/documentation/',
          ''
        );
        const category = url[1].path;
        let documentUrl = documentUrlWithCategory
          .replace(category, '')
          .slice(1);
        const document = documentUrl.length
          ? documentUrl.slice(documentUrl.lastIndexOf('/') + 1)
          : '';

        this.activeUrl = this.router.url;
        this.activeMenuItem = {
          name: categories.find((categoryItem) => categoryItem.url === category)
            ?.name,
          url: category,
        };
        this.showContent = !!document;

        const filterdLinks = links.filter(
          (link) =>
            link.route.includes(category) && !link.route.endsWith(category)
        );

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
                    ? filterdLinks.find((link) => link.title === document)?.[
                        'documentName'
                      ]
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
              name: link['documentName'],
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
        name: unhandledRouteSegments.length
          ? routeSegments[0]
          : link['documentName'],
        children: new Map(),
      };
      tree.set(routeSegments[0], menuItem);
    }

    if (unhandledRouteSegments.length) {
      this.buildMenuSubTree(menuItem.children, unhandledRouteSegments, link);
    }
  }

  private convertToArray(manuMap: Map<string, MenuTreeItem>): MenuItem[] {
    return [...manuMap].map(([_key, value]) => {
      const menuItem: MenuItem = { url: value.url, name: value.name };
      if (value.children && value.children.size) {
        menuItem.children = this.convertToArray(value.children);
      }
      return menuItem;
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
}
