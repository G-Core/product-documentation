import { EventEmitter, Injectable } from '@angular/core';
import { BehaviorSubject, Observable, Subject } from 'rxjs';

@Injectable()
export class MenuService {
    private emitToggleMenu = new Subject<any>();
    private searchPageLeave = new Subject<void>();
    private isLoginModalOpenSubject = new BehaviorSubject<boolean>(false);
    private isHostingSubject = new BehaviorSubject<boolean>(false);

    public toggleMenuEmitted$ = this.emitToggleMenu.asObservable();
    public searchPageLeave$ = this.searchPageLeave.asObservable();
    public isLoginModalOpen$: Observable<boolean> = this.isLoginModalOpenSubject.asObservable();
    public isHosting$: Observable<boolean> = this.isHostingSubject.asObservable();

    constructor() {}

    public toggleMenu(event: Event): void {
        this.emitToggleMenu.next(event);
    }

    public leaveSearchPage(): void {
        this.searchPageLeave.next();
    }

    public setCurrentUrl(isInclude: boolean): void {
        this.isHostingSubject.next(isInclude);
    }

    public setIsLoginModalOpen(isOpen: boolean): void {
        this.isLoginModalOpenSubject.next(isOpen);
    }
}
