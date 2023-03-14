import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable()
export class MenuService {
    private emitToggleMenu = new Subject<any>();

    public toggleMenuEmitted$ = this.emitToggleMenu.asObservable();

    constructor() {}

    public toggleMenu(event: Event): void {
        this.emitToggleMenu.next(event);
    }
}
