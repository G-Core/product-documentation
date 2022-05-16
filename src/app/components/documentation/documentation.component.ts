import { HttpClient } from '@angular/common/http';
import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ScullyRoutesService } from '@scullyio/ng-lib';
import { combineLatest, map, Observable, of } from 'rxjs';
import { categories } from '../../constants/categories-config';
import { MenuItem } from '../../models';

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

  constructor(
    private scully: ScullyRoutesService,
    private route: ActivatedRoute,
    private router: Router,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
    this.links$ = combineLatest([this.route.url, this.scully.available$]).pipe(
      map(([url, links]) => {
        const category = url[1].path;
        this.activeMenuItem = {
          name: categories.find((categoryItem) => categoryItem.url === category)
            ?.name,
          url: category,
        };
        this.showContent = !!url[2];

        const filterdLinks = links.filter(
          (link) =>
            link.route.includes(category) && !link.route.endsWith(category)
        );

        if (filterdLinks.length && !this.showContent) {
          this.router.navigateByUrl(filterdLinks[0].route);
        }

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
          breadcrumbs.push({
            name: filterdLinks.find((link) => link.title === url[2].path)?.[
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
}
