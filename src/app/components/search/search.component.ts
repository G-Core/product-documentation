import { ChangeDetectorRef, Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormArray, FormBuilder, FormGroup } from '@angular/forms';
import { SearchResponse } from '@algolia/client-search';

import { BehaviorSubject, Observable, merge, of, switchMap, tap } from 'rxjs';
import { AlgoliaService } from '../../services/algolia.service';
import { categories } from '../../constants';
import { ProductDocumentationIndex } from '../../models/ProductDocumentationIndex';
import { MenuService } from '../../services/menu.service';

@Component({
    selector: 'gc-search',
    templateUrl: './search.component.html',
    styleUrls: ['./search.component.scss'],
})
export class SearchComponent implements OnInit, OnDestroy {
    private page$: BehaviorSubject<number> = new BehaviorSubject(0);
    private matchingTextLength = 100;

    public searchResult$: Observable<SearchResponse<ProductDocumentationIndex>>;
    public categories = categories.filter((category) => category.url !== 'reseller-support');
    public categoriesMap = this.categories.reduce((map, category) => {
        map[category.url] = category.name;
        return map;
    }, {} as { [key: string]: string });

    public page: number = 0;
    public filter: string = '';
    public key: string;
    public filterForm: FormGroup;
    public streamingFilter: boolean = true;
    public webSecurityFilter: boolean = true;
    public isMenuExpanded: boolean = false;

    constructor(
        private algolia: AlgoliaService,
        private route: ActivatedRoute,
        private router: Router,
        private fb: FormBuilder,
        private menuService: MenuService,
        private changeDetectorRef: ChangeDetectorRef,
    ) {}

    public ngOnInit(): void {
        this.menuService.toggleMenuEmitted$.subscribe(() => {
            this.isMenuExpanded = !this.isMenuExpanded;
            this.changeDetectorRef.detectChanges();
        });
        this.filterForm = this.fb.group({
            product: this.fb.array(this.categories.map(() => this.fb.control(true))),
        });
        const filterForm$ = this.filterForm.valueChanges.pipe(
            tap((value) => {
                this.page = 0;
                this.filter = value.product
                    .map((controlValue: boolean, index: number) => (controlValue ? false : this.categories[index].url))
                    .filter((product: string) => product)
                    .map((filter: string) => `NOT product:${filter}`)
                    .join(' AND ');
            }),
        );
        const routeParam$ = this.route.queryParams.pipe(
            tap(({ key }) => {
                this.key = key ? decodeURI(key) : key;
                this.page = 0;
            }),
        );

        this.searchResult$ = merge(filterForm$, routeParam$, this.page$).pipe(
            switchMap(() =>
                this.key ? this.algolia.search(this.key, { page: this.page, filters: this.filter }) : of(null),
            ),
        );
    }

    public ngOnDestroy(): void {
        this.menuService.leaveSearchPage();
    }

    public getPagesArray(length: number): Array<void> {
        return Array(length);
    }

    public changePage(pageNumber: number): void {
        this.page = pageNumber;
        this.page$.next(pageNumber);
    }

    public selectAll(value: boolean): void {
        const formArray = this.filterForm.get('product') as FormArray;
        formArray.patchValue(formArray.controls.map(() => value));
    }

    public search(key: string): void {
        this.router.navigate(['/search'], {
            queryParams: { key: encodeURI(key.trim()) },
        });
    }

    public getMatchingText(content: string): string {
        const targetIndex = content.indexOf('<em>');
        if (targetIndex === -1) {
            return '';
        }

        const contentWithoutNewLines = content.replace(/\n/g, ' ');

        if (targetIndex < this.matchingTextLength / 2) {
            return `${contentWithoutNewLines
                .slice(0, this.matchingTextLength)
                .trim()
                .split(' ')
                .slice(0, -1)
                .join(' ')}`;
        } else {
            return `${contentWithoutNewLines
                .slice(targetIndex - this.matchingTextLength / 2, targetIndex + this.matchingTextLength / 2)
                .trim()
                .split(' ')
                .slice(1, -1)
                .join(' ')}`;
        }
    }
}
