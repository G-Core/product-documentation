import { Component } from '@angular/core';
import { ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { Observable } from 'rxjs';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
})
export class AppComponent {
    public links$: Observable<Array<ScullyRoute>> = this.scully.available$;

    constructor(private scully: ScullyRoutesService) {}
}
