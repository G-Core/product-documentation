import {
    AfterViewInit,
    ChangeDetectionStrategy,
    Component,
    ElementRef,
    Input,
    NgZone,
    Renderer2,
    ViewChild,
} from '@angular/core';

@Component({
    selector: 'gc-exandable-element',
    templateUrl: './exandable-element.component.html',
    styleUrls: ['./exandable-element.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ExandableElementComponent implements AfterViewInit {
    @Input() public title: string = '';

    public isExpanded: boolean = false;

    @ViewChild('titleElement') public titleElement: ElementRef;

    constructor(private ngZone: NgZone, private renderer: Renderer2) {}

    public ngAfterViewInit(): void {
        this.ngZone.runOutsideAngular(() => {
            this.renderer.listen(this.titleElement.nativeElement, 'click', () => this.toggle());
        });
    }

    public toggle(): void {
        this.isExpanded = !this.isExpanded;
        if (this.isExpanded) {
            this.renderer.addClass(this.titleElement.nativeElement, 'expanded');
            this.renderer.addClass(this.titleElement.nativeElement.nextElementSibling, 'expanded');
        } else {
            this.renderer.removeClass(this.titleElement.nativeElement, 'expanded');
            this.renderer.removeClass(this.titleElement.nativeElement.nextElementSibling, 'expanded');
        }
    }
}
