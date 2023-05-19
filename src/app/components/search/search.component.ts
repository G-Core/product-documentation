import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup } from '@angular/forms';
import { SearchResponse } from '@algolia/client-search';

import { Observable, of, switchMap, tap } from 'rxjs';
import { AlgoliaService } from '../../services/algolia.service';
import { categories } from '../../constants';
import { ProductDocumentationIndex } from '../../models/ProductDocumentationIndex';

@Component({
    selector: 'gc-search',
    templateUrl: './search.component.html',
    styleUrls: ['./search.component.scss'],
})
export class SearchComponent implements OnInit {
    public searchResult$: Observable<SearchResponse<ProductDocumentationIndex>>;
    public categories = categories;
    public categoriesMap = categories.reduce((map, category) => {
        map[category.name] = category.url;
        return map;
    }, {} as { [key: string]: string });

    public page: number = 0;
    public filter: string = '';
    public key: string;
    public filterForm: FormGroup;
    public streamingFilter: boolean = true;
    public webSecurityFilter: boolean = true;

    constructor(private algolia: AlgoliaService, private route: ActivatedRoute, private fb: FormBuilder) {}

    public ngOnInit(): void {
        this.filterForm = this.fb.group({
            product: this.fb.array(categories.map(() => this.fb.control(true))),
        });
        this.filterForm.valueChanges.subscribe((value) => {
            this.page = 0;
            this.filter = value.product
                .map((controlValue: boolean, index: number) => (controlValue ? false : categories[index].name))
                .filter((product: string) => product)
                .map((filter: string) => `NOT product:${filter}`)
                .join(' AND ');

            this.searchResult$ = this.algolia.search(this.key, { filters: this.filter });
        });
        this.searchResult$ = this.route.queryParams.pipe(
            tap(({ key }) => (this.key = decodeURI(key))),
            switchMap(({ key }) => (key ? this.algolia.search(decodeURI(key)) : of(null))),
        );
    }

    public getPagesArray(length: number): Array<void> {
        return Array(length);
    }

    public changePage(pageNumber: number): void {
        this.page = pageNumber;
        this.searchResult$ = this.algolia.search(this.key, { page: pageNumber, filters: this.filter });
    }
}
