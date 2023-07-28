import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnDestroy, OnInit } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
import { filter, Observable, Subject, takeUntil } from 'rxjs';

import { MenuService } from '../../services/menu.service';
import { environment } from '../../../environments/environment';

@Component({
    selector: 'gc-header',
    templateUrl: './header.component.html',
    styleUrls: ['./header.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HeaderComponent implements OnInit, OnDestroy {
    private destroy$: Subject<void> = new Subject();

    public baseHref: string = environment.baseHref;
    public searchKey: string;
    public isHosting: boolean = false;
    public isLoginModalOpen: boolean = false;

    constructor(private menuService: MenuService, private router: Router, private cd: ChangeDetectorRef) {}

    public ngOnInit(): void {
        this.menuService.searchPageLeave$.pipe(takeUntil(this.destroy$)).subscribe(() => {
            this.searchKey = '';
            this.cd.detectChanges();
        });

        this.router.events
            .pipe(
                filter((event) => event instanceof NavigationEnd),
                takeUntil(this.destroy$),
            )
            .subscribe((event) => {
                const currentUrl = this.router.url;
                this.isHosting = currentUrl.includes('/hosting');
                this.menuService.setCurrentUrl(this.isHosting);
                this.cd.detectChanges();
            });

        this.menuService.isLoginModalOpen$.pipe(takeUntil(this.destroy$)).subscribe((isOpen) => {
            this.isLoginModalOpen = isOpen;
            this.cd.detectChanges();
        });
    }

    public ngOnDestroy(): void {
        this.destroy$.next();
        this.destroy$.complete();
    }

    public toggleMenu(event: Event): void {
        this.menuService.toggleMenu(event);
    }

    public search(): void {
        this.router.navigate(['/search'], {
            queryParams: { key: encodeURI(this.searchKey.trim()) },
        });
    }

    public login(): void {
        this.menuService.setIsLoginModalOpen(true);
        this.cd.detectChanges();
    }
}
