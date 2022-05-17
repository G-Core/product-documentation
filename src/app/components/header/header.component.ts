import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'gc-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HeaderComponent {
  isMenuExpanded: boolean;

  toggleMenu(): void {
    this.isMenuExpanded = !this.isMenuExpanded;
  }
}
