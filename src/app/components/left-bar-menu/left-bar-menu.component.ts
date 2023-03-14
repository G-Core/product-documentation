import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { MenuItem } from '../../models';
import { MenuService } from '../../services/menu.service';

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

    constructor(private clickDetection: MenuService) {}

    public toggleMenu(event: Event): void {
        this.clickDetection.toggleMenu(event);
    }
}
