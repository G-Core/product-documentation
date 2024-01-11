import {
    AfterViewInit,
    ChangeDetectionStrategy,
    ChangeDetectorRef,
    Component,
    ElementRef,
    Input,
    NgZone,
    OnChanges,
    OnInit,
    Renderer2,
    SimpleChanges,
    ViewChild,
} from '@angular/core';

import { MenuItem } from '../../../models';
import { MenuService } from '../../../services/menu.service';

@Component({
    selector: 'gc-dropdown-menu-item',
    templateUrl: './dropdown-menu-item.component.html',
    styleUrls: ['./dropdown-menu-item.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DropdownMenuItemComponent implements OnInit, OnChanges, AfterViewInit {
    @Input() public menuItem: MenuItem;
    @Input() public activeUrl: string = '';

    public isExpanded: boolean = false;
    public menuItemDisplayName: string = '';

    @ViewChild('menuDropdown') public menuDropdown: ElementRef;

    constructor(
        private ngZone: NgZone,
        private renderer: Renderer2,
        private changeDetector: ChangeDetectorRef,
        private menuService: MenuService,
    ) {}

    public ngOnChanges(changes: SimpleChanges): void {
        if (changes.activeUrl) {
            this.isExpanded = this.hasActiveChildItem(
                changes.menuItem?.currentValue || this.menuItem,
                changes.activeUrl.currentValue,
            );
        }
    }

    public ngOnInit(): void {
        this.menuItemDisplayName = this.menuItem.name || this.menuItem.title.split('-').join(' ');
    }

    public ngAfterViewInit(): void {
        this.ngZone.runOutsideAngular(() => {
            this.renderer.listen(this.menuDropdown.nativeElement, 'click', () => {
                this.toggleMenu();
            });
        });
    }

    public toggleMenu(): void {
        this.isExpanded = !this.isExpanded;
        this.changeDetector.detectChanges();
    }

    public toggleSideMenu(event: Event): void {
        this.menuService.toggleMenu(event);
    }

    private hasActiveChildItem(menuItem: MenuItem, activeUrl: string): boolean {
        return (
            (menuItem.url && activeUrl?.endsWith(menuItem.url)) ||
            menuItem.children?.some((childMenuItem) => this.hasActiveChildItem(childMenuItem, activeUrl))
        );
    }
}
