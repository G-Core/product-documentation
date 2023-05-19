import { ChangeDetectionStrategy, Component } from '@angular/core';
import { Router } from '@angular/router';
import { MenuService } from '../../services/menu.service';

@Component({
    selector: 'gc-header',
    templateUrl: './header.component.html',
    styleUrls: ['./header.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HeaderComponent {
    public searchKey: string;

    constructor(private clickDetection: MenuService, private router: Router) {}

    public toggleMenu(event: Event): void {
        this.clickDetection.toggleMenu(event);
    }

    public search(): void {
        this.router.navigate(['/search'], {
            queryParams: { key: encodeURI(this.searchKey) },
        });
    }
}
