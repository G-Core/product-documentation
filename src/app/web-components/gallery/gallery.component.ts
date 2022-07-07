import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'gc-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.scss'],
})
export class GalleryComponent implements AfterViewInit {
  currentGalleryItemSrc: string;
  currentGalleryItemAlt: string;

  @ViewChild('gallery') gallery: ElementRef;

  ngAfterViewInit(): void {
    if (!this.currentGalleryItemSrc) {
      const images = this.gallery.nativeElement.querySelectorAll('img');
      this.currentGalleryItemAlt = images[0].getAttribute('alt');
      this.currentGalleryItemSrc = images[0].getAttribute('src');
    }
  }

  changeItem(event: any): void {
    const targetItem = event.target;
    const src = targetItem.getAttribute('src');
    const alt = targetItem.getAttribute('alt');
    if (src) {
      this.currentGalleryItemSrc = src;
      this.currentGalleryItemAlt = alt;
    }
  }
}
