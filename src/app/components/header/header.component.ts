import {ChangeDetectionStrategy, Component} from '@angular/core';
import {DataService} from "../../services/data.service";

@Component({
  selector: 'gc-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HeaderComponent {

  constructor(private data: DataService) {}

  toggleMenu(event: any) {
    this.data.emitChange(event);
  }
}
