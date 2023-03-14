import { AfterViewInit, ChangeDetectionStrategy, Component, ElementRef, ViewChild } from '@angular/core';

@Component({
    selector: 'gc-code-block',
    templateUrl: './code-block.component.html',
    styleUrls: ['./code-block.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CodeBlockComponent {}
