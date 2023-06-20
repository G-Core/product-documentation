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
            this.algoliaInstance = algoliasearch('0GWOH3DBQG', '0f8c47609b46da62bf3852876be561af');
            this.algoliaIndex = this.algoliaInstance.initIndex('product_documentation_preprod');
        }
    }

    public search(key: string, options?: SearchOptions): Observable<SearchResponse<ProductDocumentationIndex>> {
        return from(this.algoliaIndex.search<ProductDocumentationIndex>(key, { hitsPerPage: 10, ...options }));
    }
}
