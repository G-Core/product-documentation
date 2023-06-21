import { Injectable } from '@angular/core';
import algoliasearch, { SearchIndex, SearchClient } from 'algoliasearch/lite';
import { SearchResponse, SearchOptions } from '@algolia/client-search';
import { isScullyRunning } from '@scullyio/ng-lib';
import { from } from 'rxjs/internal/observable/from';
import { Observable } from 'rxjs';
import { ProductDocumentationIndex } from '../models/ProductDocumentationIndex';
import config from '../../config';

@Injectable({
    providedIn: 'root',
})
export class AlgoliaService {
    private algoliaInstance: SearchClient;
    private algoliaIndex: SearchIndex;

    constructor() {
        if (!isScullyRunning()) {
            this.algoliaInstance = algoliasearch(config.algolia_app_id, config.algolia_search_key);
            this.algoliaIndex = this.algoliaInstance.initIndex(config.aloglia_pd_index);
        }
    }

    public search(key: string, options?: SearchOptions): Observable<SearchResponse<ProductDocumentationIndex>> {
        return from(this.algoliaIndex.search<ProductDocumentationIndex>(key, { hitsPerPage: 10, ...options }));
    }
}
