import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { MenuItem } from '../../models';
import { MenuService } from '../../services/menu.service';
import { environment } from '../../../environments/environment';

@Component({
    selector: 'gc-left-bar-menu',
    templateUrl: './left-bar-menu.component.html',
    styleUrls: ['./left-bar-menu.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LeftBarMenuComponent {
    @Input() public activeMenuItem: MenuItem;
    @Input() public activeUrl: string;
    @Input() public menuItems: any;

    public baseHref: string = environment.baseHref;

    constructor(private clickDetection: MenuService) {}

    public toggleMenu(event: Event): void {
        this.clickDetection.toggleMenu(event);
    }
}
