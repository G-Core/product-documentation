import { ChangeDetectionStrategy, Component, Input, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
    selector: 'switcher',
    templateUrl: './switcher.component.html',
    styleUrls: ['./switcher.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SwitcherComponent implements OnInit {
    @Input() public leftText: string;
    @Input() public rightText: string;
    @Input() public value: string;
    @Input() public isActiveLeft: boolean;
    @Input() public isActiveRight: boolean;
    @Input() public name: string = this.getRandomName();
    @Input() public isHiddenLabels: boolean = false;
    @Input() public isLeftDisabled: boolean = false;
    @Input() public variant: 'contrast' | 'violet' | 'orange-gray' | 'orange-transparent';
    @Output() public valueChange: EventEmitter<string> = new EventEmitter<string>();

    public ngOnInit(): void {
        this.value = this.value || this.leftText;
    }

    public onChange(e: any): void {
        this.value = e.target.value;
        this.valueChange.emit(this.value);
    }

    private getRandomName(): string {
        const random = Math.round(Math.random() * 1000);
        return `name${random}`;
    }
}
