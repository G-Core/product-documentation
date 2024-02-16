import {
    ChangeDetectionStrategy,
    ChangeDetectorRef,
    Component,
    HostBinding,
    Input,
    OnDestroy,
    OnInit,
} from '@angular/core';
import { Router } from '@angular/router';
import { Subject, takeUntil } from 'rxjs';
import { MenuItem } from '../../models';
import { MenuService } from '../../services/menu.service';
import { environment } from '../../../environments/environment';

@Component({
    selector: 'gc-left-bar-menu',
    templateUrl: './left-bar-menu.component.html',
    styleUrls: ['./left-bar-menu.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LeftBarMenuComponent implements OnInit, OnDestroy {
    @Input() public activeMenuItem: MenuItem;
    @Input() public activeUrl: string;
    @Input() public menuItems: any;
    @Input() public isHomePage: boolean = false;
    @HostBinding('class.with-disclaimer') public isNotResellerPage: boolean = false;

    private destroy$: Subject<void> = new Subject();

    public baseHref: string = environment.baseHref;
    public isHosting: boolean = false;

    constructor(private menuService: MenuService, private router: Router, private cd: ChangeDetectorRef) {}

    public ngOnInit(): void {
        this.menuService.isHosting$.pipe(takeUntil(this.destroy$)).subscribe((isHosting) => {
            this.isHosting = isHosting;
            this.isNotResellerPage = !this.router.url.includes('reseller-support');
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

    public openModal(): void {
        this.toggleMenu(event);
        this.menuService.setIsLoginModalOpen(true);
        this.cd.detectChanges();
    }
}
