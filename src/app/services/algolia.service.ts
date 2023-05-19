import { Injectable } from '@angular/core';
import algoliasearch, { SearchIndex, SearchClient } from 'algoliasearch/lite';
import { SearchResponse, SearchOptions } from '@algolia/client-search';
import { isScullyRunning } from '@scullyio/ng-lib';
import { from } from 'rxjs/internal/observable/from';
import { Observable } from 'rxjs';
import { ProductDocumentationIndex } from '../models/ProductDocumentationIndex';

@Injectable({
    providedIn: 'root',
})
export class AlgoliaService {
    private algoliaInstance: SearchClient;
    private algoliaIndex: SearchIndex;

    constructor() {
        if (!isScullyRunning()) {
            this.algoliaInstance = algoliasearch('1U59KUGBCD', '9edc35d8b4fe6e761d4ac4fe71070ce3');
            this.algoliaIndex = this.algoliaInstance.initIndex('gcore_site');
        }
    }

    public search(key: string, options?: SearchOptions): Observable<SearchResponse<ProductDocumentationIndex>> {
        return from(this.algoliaIndex.search<ProductDocumentationIndex>(key, options));
    }
}
