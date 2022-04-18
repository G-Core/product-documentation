import { Component, ViewEncapsulation } from '@angular/core';
import { ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { map, Observable } from 'rxjs';

declare var ng: any;

@Component({
  selector: 'app-documentation',
  templateUrl: './documentation.component.html',
  preserveWhitespaces: true,
  styleUrls: ['./documentation.component.scss'],
  encapsulation: ViewEncapsulation.Emulated,
})
export class DocumentationComponent {
  links$: Observable<ScullyRoute[]> = this.scully.available$.pipe(
    map((links) =>
      links.filter((link) => link.route.startsWith('/documentation/'))
    )
  );

  constructor(private scully: ScullyRoutesService) {}
}
