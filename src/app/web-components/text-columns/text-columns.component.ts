import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
    selector: 'gc-text-columns',
    templateUrl: './text-columns.component.html',
    styleUrls: ['./text-columns.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class TextColumnsComponent {}
