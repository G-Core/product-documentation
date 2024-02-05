import { Component, Input } from '@angular/core';

type AlertType = 'tip' | 'info' | 'warning' | 'caution';

@Component({
    selector: 'gc-alert-element',
    templateUrl: './alert-element.component.html',
    styleUrls: ['./alert-element.component.scss'],
})
export class AlertElementComponent {
    @Input() public type: AlertType = 'tip';
    @Input() public title: string = '';
    @Input() public isShowLinks = false;
    public svgNames: { [key: string]: string } = {
        tip: 'check-circle',
        info: 'info-circle',
        warning: 'info-circle',
        caution: 'close-red',
    };
}
