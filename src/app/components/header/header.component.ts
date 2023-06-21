import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Subject, takeUntil } from 'rxjs';

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

    constructor(private menuService: MenuService, private router: Router, private cd: ChangeDetectorRef) {}

    public ngOnInit(): void {
        this.menuService.searchPageLeave$.pipe(takeUntil(this.destroy$)).subscribe(() => {
            this.searchKey = '';
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
}
