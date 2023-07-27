import { ChangeDetectionStrategy, ChangeDetectorRef, Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MenuItem } from '../../models';
import { MenuService } from '../../services/menu.service';
import { environment } from '../../../environments/environment';

@Component({
    selector: 'gc-left-bar-menu',
    templateUrl: './left-bar-menu.component.html',
    styleUrls: ['./left-bar-menu.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LeftBarMenuComponent implements OnInit {
    @Input() public activeMenuItem: MenuItem;
    @Input() public activeUrl: string;
    @Input() public menuItems: any;
    @Input() public isHomePage: boolean = false;

    public baseHref: string = environment.baseHref;
    public isHosting: boolean = false;

    constructor(private clickDetection: MenuService, private router: Router, private cd: ChangeDetectorRef) {}

    public ngOnInit(): void {
        this.isHosting = this.clickDetection.isHosting;
        this.cd.detectChanges();
    }

    public toggleMenu(event: Event): void {
        this.clickDetection.toggleMenu(event);
    }

    public openModal(): void {
        this.toggleMenu(event);
        this.clickDetection.setIsLoginModalOpen(true);
        this.cd.detectChanges();
    }
}
