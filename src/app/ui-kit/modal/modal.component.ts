import { ChangeDetectionStrategy, Component, EventEmitter, Input, Output } from '@angular/core';
import { ModalSize, ModalTheme } from './modal.interface';

@Component({
    selector: 'gcore-modal',
    templateUrl: './modal.component.html',
    styleUrls: ['./modal.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ModalComponent {
    @Input() public isOpen: boolean;
    @Input() public size: string = 'medium';
    @Input() public scrollable: boolean = true;
    @Input() public minPaddings: boolean = true;
    @Output() public isOpenChange = new EventEmitter<boolean>();

    public showModal($event: MouseEvent): void {
        $event.stopPropagation();
        this.isOpenChange.emit(!this.isOpenChange);
    }
}
