import { ChangeDetectionStrategy, Component } from '@angular/core';
import { categories } from '../../constants/categories-config';
import { Category } from '../../models';

@Component({
  selector: 'gc-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomeComponent {
  categories: Category[] = categories;
}
