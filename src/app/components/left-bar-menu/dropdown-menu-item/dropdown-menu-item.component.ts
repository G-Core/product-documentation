import {
  ChangeDetectionStrategy,
  Component,
  Input,
  OnChanges,
  OnInit,
  SimpleChanges,
} from '@angular/core';
import { MenuItem } from '../../../models';

@Component({
  selector: 'gc-dropdown-menu-item',
  templateUrl: './dropdown-menu-item.component.html',
  styleUrls: ['./dropdown-menu-item.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DropdownMenuItemComponent implements OnInit, OnChanges {
  @Input() menuItemName: string;
  @Input() menuItems: MenuItem[] = [];
  @Input() activeUrl: string = '';

  isExpanded: boolean = false;
  menuItemDisplayName: string = '';

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['activeUrl']) {
      this.isExpanded =
        changes['activeUrl'].currentValue &&
        changes['activeUrl'].currentValue
          .split('/')
          .includes(changes['menuItemName']?.currentValue || this.menuItemName);
    }
  }

  ngOnInit(): void {
    this.menuItemDisplayName = this.menuItemName.split('-').join(' ');
  }

  toggleMenu(): void {
    this.isExpanded = !this.isExpanded;
  }
}
