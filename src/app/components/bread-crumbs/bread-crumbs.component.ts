import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { Router } from '@angular/router';
import { MenuItem } from '../../models';

@Component({
    selector: 'gc-bread-crumbs',
    templateUrl: './bread-crumbs.component.html',
    styleUrls: ['./bread-crumbs.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class BreadCrumbsComponent {
    @Input() public items: Array<MenuItem>;

    constructor(private router: Router) {}
}
