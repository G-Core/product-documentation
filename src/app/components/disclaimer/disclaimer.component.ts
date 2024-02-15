import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
    selector: 'gc-disclaimer',
    templateUrl: './disclaimer.component.html',
    styleUrls: ['./disclaimer.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DisclaimerComponent {}
