import { Directive, ElementRef, Renderer2, OnChanges, Input } from '@angular/core';
import { MenuService } from '../../services/menu.service';

@Directive({
    selector: '[hideIfUrlContains]',
})
export class HideIfUrlContainsDirective implements OnChanges {
    @Input('hideIfUrlContains') public showModal: boolean;

    constructor(private elementRef: ElementRef, private renderer: Renderer2, private menuService: MenuService) {}

    public ngOnChanges(): void {
        const url = this.menuService.getCurrentUrl();
        const hideElement = (url && url.includes('/hosting')) || !this.showModal;
        this.renderer.setProperty(this.elementRef.nativeElement, 'hidden', hideElement);
    }
}
