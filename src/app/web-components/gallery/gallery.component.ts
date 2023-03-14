import {
    AfterViewInit,
    ChangeDetectionStrategy,
    ChangeDetectorRef,
    Component,
    ElementRef,
    NgZone,
    Renderer2,
    ViewChild,
} from '@angular/core';

@Component({
    selector: 'gc-gallery',
    templateUrl: './gallery.component.html',
    styleUrls: ['./gallery.component.scss'],
})
export class GalleryComponent implements AfterViewInit {
    public currentGalleryItemSrc: string;
    public currentGalleryItemAlt: string;
    public isActive: boolean = false;
    public currentIndex: number = 0;
    public sliderCount: number = 0;

    @ViewChild('gallery') public gallery: ElementRef;
    @ViewChild('prevButton') public prevButton: ElementRef;
    @ViewChild('nextButton') public nextButton: ElementRef;

    constructor(private renderer: Renderer2, private ngZone: NgZone, private cd: ChangeDetectorRef) {}

    public ngAfterViewInit(): void {
        if (!this.currentGalleryItemSrc) {
            const images = [...this.gallery.nativeElement.querySelectorAll('img')];
            this.sliderCount = images.length;

            images.forEach((item: HTMLElement, index: number) => {
                this.renderer.setAttribute(item, 'data-index', `${index}`);
            });

            this.setActiveSlide(0);
        }

        this.ngZone.runOutsideAngular(() => {
            this.renderer.listen(this.gallery.nativeElement, 'click', (event) => this.changeItem(event));
            this.renderer.listen(this.prevButton.nativeElement, 'click', () => this.goToPrevious());
            this.renderer.listen(this.nextButton.nativeElement, 'click', () => this.goToNext());
        });
    }

    public changeItem(event: any): void {
        const targetItem = event.target;
        this.currentIndex = Number(targetItem.dataset.index);
        this.setActiveSlide(this.currentIndex);
        this.cd.detectChanges();
    }

    public goToPrevious(): void {
        const itemsArray = [...this.gallery.nativeElement.querySelectorAll('img')];
        itemsArray.forEach((_item: HTMLElement, index) => {
            if (index === this.currentIndex && index > 0) {
                this.setActiveSlide(index - 1);
            }
        });
        if (this.currentIndex > 0) {
            this.currentIndex = this.currentIndex - 1;
        }

        this.transformSlides();
        this.cd.detectChanges();
    }

    public goToNext(): void {
        const itemsArray = [...this.gallery.nativeElement.querySelectorAll('img')];
        const arrayLength = itemsArray.length - 1;
        itemsArray.forEach((_item: HTMLElement, index) => {
            if (index === this.currentIndex && index + 1 <= arrayLength) {
                this.setActiveSlide(index + 1);
            }
        });

        if (this.currentIndex < arrayLength) {
            this.currentIndex = this.currentIndex + 1;
        }

        this.transformSlides();
        this.cd.detectChanges();
    }

    private setActiveSlide(currentIndex: number): void {
        const itemsArray = [...this.gallery.nativeElement.querySelectorAll('img')];

        itemsArray.forEach((item: HTMLElement) => {
            this.renderer.removeClass(item, 'active');
        });

        itemsArray.forEach((item: HTMLElement, index) => {
            if (index === currentIndex) {
                const src = item.getAttribute('src');
                const alt = item.getAttribute('alt');
                this.renderer.addClass(item, 'active');

                if (src) {
                    this.currentGalleryItemSrc = src;
                    this.currentGalleryItemAlt = alt;
                }
            }
        });
    }

    private transformSlides(): void {
        const galleryInner = [...this.gallery.nativeElement.querySelectorAll('p')];
        let transformValue = 0;
        if (this.currentIndex > 3) {
            transformValue = (this.currentIndex - 3) * 25;
        } else {
            transformValue = 0;
        }

        galleryInner.forEach((item: HTMLElement) => {
            this.renderer.setStyle(item, 'transform', `translateX(-${transformValue}%)`);
            this.renderer.setStyle(item, 'transition', '0.5s');
        });
    }
}
