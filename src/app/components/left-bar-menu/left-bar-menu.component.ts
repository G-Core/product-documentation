import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { MenuItem } from '../../models';

@Component({
  selector: 'gc-left-bar-menu',
  templateUrl: './left-bar-menu.component.html',
  styleUrls: ['./left-bar-menu.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LeftBarMenuComponent {
  @Input() activeMenuItem: MenuItem;
  @Input() menuItems: MenuItem[];
}
