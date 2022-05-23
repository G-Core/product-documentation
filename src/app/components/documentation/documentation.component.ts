import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ScullyRoutesService } from '@scullyio/ng-lib';
import { combineLatest, map, Observable, of, take } from 'rxjs';
import { categories, DOCS_GITHUB_REPO } from '../../constants';
import { MenuItem } from '../../models';
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
  showContent: boolean;
  breadCrumbs: MenuItem[] = [];
  githubUrl: string;
  lastModifiedLabel: string = '';

  constructor(
    private scully: ScullyRoutesService,
    private route: ActivatedRoute,
    private githubApiService: GitHubAPIService
  ) {}

  ngOnInit(): void {
    this.links$ = combineLatest([this.route.url, this.scully.available$]).pipe(
      map(([url, links]) => {
        const category = url[1]?.path;
        const document = url[2]?.path;
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
          this.githubUrl = `${DOCS_GITHUB_REPO}${category}/${document}.md`;
          this.setLastModifiedDate(`documentation/${category}/${document}`);
          breadcrumbs.push({
            name: filterdLinks.find((link) => link.title === document)?.[
              'documentName'
            ],
            url: '',
          });
        }

        this.breadCrumbs = breadcrumbs;

        return filterdLinks.map((link) => ({
          url: link.route,
          name: link['documentName'],
        }));
      })
    );
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
