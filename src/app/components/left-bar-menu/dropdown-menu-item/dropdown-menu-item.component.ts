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
import { Router } from '@angular/router';

import { MenuItem } from '../../../models';

@Component({
    selector: 'gc-dropdown-menu-item',
    templateUrl: './dropdown-menu-item.component.html',
    styleUrls: ['./dropdown-menu-item.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DropdownMenuItemComponent implements OnInit, OnChanges, AfterViewInit {
    @Input() public menuItemName: string;
    @Input() public menuItemTitle: string;
    @Input() public menuItems: Array<MenuItem> = [];
    @Input() public activeUrl: string = '';
    @Input() public menuUrl: string = '';

    public isExpanded: boolean = false;
    public menuItemDisplayName: string = '';

    @ViewChild('menuDropdown') public menuDropdown: ElementRef;

    constructor(private ngZone: NgZone, private renderer: Renderer2, private changeDetector: ChangeDetectorRef) {}

    public ngOnChanges(changes: SimpleChanges): void {
        if (changes.activeUrl) {
            this.isExpanded =
                changes.activeUrl.currentValue &&
                changes.activeUrl.currentValue
                    .split('/')
                    .includes(changes.menuItemTitle?.currentValue || this.menuItemTitle);
        }
    }

    public ngOnInit(): void {
        this.menuItemDisplayName = this.menuItemName || this.menuItemTitle.split('-').join(' ');
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
}
