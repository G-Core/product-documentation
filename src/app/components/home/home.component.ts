import { AfterViewInit, ChangeDetectionStrategy, ChangeDetectorRef, Component, Input, OnInit } from '@angular/core';
import { categories } from '../../constants/categories-config';
import { Category, MenuItem } from '../../models';
import { environment } from '../../../environments/environment';
import { MenuService } from '../../services/menu.service';

@Component({
    selector: 'gc-home',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomeComponent implements OnInit {
    public categories: Array<Category> = categories;
    public baseHref: string = environment.baseHref;
    public isMenuExpanded: boolean = false;

    constructor(private changeDetectorRef: ChangeDetectorRef, private data: MenuService) {}

    public ngOnInit(): void {
        this.data.toggleMenuEmitted$.subscribe(() => {
            this.isMenuExpanded = !this.isMenuExpanded;
            this.changeDetectorRef.detectChanges();
        });

        window.scrollTo({ top: 0, behavior: 'auto' });
    }
}
