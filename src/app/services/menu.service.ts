import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable()
export class MenuService {
    private emitToggleMenu = new Subject<any>();
    private searchPageLeave = new Subject<void>();

    public toggleMenuEmitted$ = this.emitToggleMenu.asObservable();
    public searchPageLeave$ = this.searchPageLeave.asObservable();

    constructor() {}

    public toggleMenu(event: Event): void {
        this.emitToggleMenu.next(event);
    }

    public leaveSearchPage(): void {
        this.searchPageLeave.next();
    }
}
