import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { combineLatest, map, Observable, of, tap } from 'rxjs';

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
  showContent: boolean = false;

  constructor(
    private scully: ScullyRoutesService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.links$ = combineLatest([this.route.url, this.scully.available$]).pipe(
      map(([url, links]) => {
        this.category = url[0].path;
        this.showContent = !!url[1];

        return links.filter(
          (link) =>
            link.route.startsWith('/documentation/') &&
            link.route.includes(this.category) &&
            !link.route.endsWith(this.category)
        );
      })
    );
  }
}
