import {
    ChangeDetectionStrategy,
    Component,
    EventEmitter,
    Input,
    OnChanges,
    OnInit,
    Output,
    SimpleChanges,
} from '@angular/core';

@Component({
    selector: 'gc-pagination',
    templateUrl: './pagination.component.html',
    styleUrls: ['./pagination.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PaginationComponent implements OnInit, OnChanges {
    @Input() public pages: Array<void> = [];
    @Input() public currentPage: number = 0;

    @Output() public changePage: EventEmitter<number> = new EventEmitter();

    public disableArrLeft: boolean = false;
    public disableArrRight: boolean = false;

    public ngOnInit(): void {
        this.setPage(this.currentPage);
    }

    public ngOnChanges(changes: SimpleChanges): void {
        if (changes.currentPage) {
            this.setPage(changes.currentPage.currentValue);
        }
    }

    public setPage(page: number): void {
        if (this.currentPage === page) {
            return;
        }
        this.currentPage = page;
        this.disableArrRight = this.currentPage === this.pages.length - 1;
        this.disableArrLeft = this.currentPage === 0;
        this.changePage.emit(page);
    }
}
