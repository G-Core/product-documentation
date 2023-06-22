import { ChangeDetectionStrategy, Component } from '@angular/core';
import { categories } from '../../constants/categories-config';
import { Category } from '../../models';
import { environment } from '../../../environments/environment';

@Component({
    selector: 'gc-home',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomeComponent {
    public categories: Array<Category> = categories;
    public baseHref: string = environment.baseHref;
}
