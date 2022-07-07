import { Component, Input } from '@angular/core';

@Component({
  selector: 'gc-exandable-element',
  templateUrl: './exandable-element.component.html',
  styleUrls: ['./exandable-element.component.scss'],
})
export class ExandableElementComponent {
  @Input() title: string = '';

  isExpanded: boolean = false;

  toggle(): void {
    this.isExpanded = !this.isExpanded;
  }
}
