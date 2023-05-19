import { Component, forwardRef } from '@angular/core';
import { ControlValueAccessor, NG_VALUE_ACCESSOR } from '@angular/forms';

@Component({
    selector: 'gc-search-box',
    templateUrl: './search-box.component.html',
    styleUrls: ['./search-box.component.scss'],
    providers: [
        {
            provide: NG_VALUE_ACCESSOR,
            useExisting: forwardRef(() => SearchBoxComponent),
            multi: true,
        },
    ],
})
export class SearchBoxComponent implements ControlValueAccessor {
    public onChange: Function;
    public onTouched: Function;
    public searchKey: string;

    constructor() {}

    public onChanges(searchKey: string): void {
        this.onChange(searchKey);
    }

    public registerOnChange(fn: Function): void {
        this.onChange = fn;
    }

    public registerOnTouched(fn: Function): void {
        this.onTouched = fn;
    }

    public writeValue(searchKey: string): void {
        this.searchKey = searchKey;
    }
}
