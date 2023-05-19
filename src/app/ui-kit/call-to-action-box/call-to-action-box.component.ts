import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { CallToActionBoxContent } from './call-to-action-box-content';

@Component({
    selector: 'gc-call-to-action-box',
    templateUrl: './call-to-action-box.component.html',
    styleUrls: ['./call-to-action-box.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CallToActionBoxComponent {
    @Input() public content: CallToActionBoxContent;
}
