import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { combineLatest, map, Observable, of, tap } from 'rxjs';

declare var ng: any;

@Component({
  selector: 'app-documentation',
  templateUrl: './documentation.component.html',
  preserveWhitespaces: true,
  styleUrls: ['./documentation.component.scss'],
  encapsulation: ViewEncapsulation.Emulated,
})
export class DocumentationComponent implements OnInit {
  links$: Observable<ScullyRoute[]> = of([]);
  category: string = '';

  constructor(
    private scully: ScullyRoutesService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.links$ = combineLatest([this.route.url, this.scully.available$]).pipe(
      map(([url, links]) => {
        this.category = url[0].path;
        const filteredLinks = links.filter(
          (link) =>
            link.route.startsWith('/documentation/') &&
            link.route.includes(this.category) &&
            !link.route.endsWith(this.category)
        );
        if (filteredLinks[0] && url.length === 1) {
          this.router.navigateByUrl(filteredLinks[0].route);
        }
        return filteredLinks;
      })
    );
  }
}
