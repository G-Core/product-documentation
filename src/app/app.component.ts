import {Component} from '@angular/core';
import { ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})
export class AppComponent {
  links$: Observable<ScullyRoute[]> = this.scully.available$;

  constructor(private scully: ScullyRoutesService) {}

  ngOnInit() {}

}
