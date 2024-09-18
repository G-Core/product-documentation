import * as fs from 'fs';
import { join } from 'path';
import crypto from 'crypto';
import { log, green, red, logError, HandledRoute, scullyConfig } from '@scullyio/scully';
import algoliasearch, { SearchClient } from 'algoliasearch';
import { JSDOM } from 'jsdom';

interface Payload {
    title: string;
    menuTitle: string;
    mainTitle: string;
    content: string;
    url: string;
    product: string;
    objectID: number;
}

const INDEX_NAME = process.env.ALGOLIA_PD_INDEX;
const SCULLY_CODE = "try {window['scullyContent']";

function getPageContent(document: any): string {
    const text = document.querySelector('.scully-container').textContent;
    const scullyCodeIndex = text.indexOf(SCULLY_CODE);
    if (scullyCodeIndex !== -1) {
        return text.slice(0, scullyCodeIndex).trim();
    }
    return text.trim();
}

function initAlgoliaClient(): SearchClient {
    let isError = false;
    const appId = process.env.ALGOLIA_APP_ID;
    const apiKey = process.env.ALGOLIA_WRITE_KEY;

    if (!appId) {
        logError(red(`ALGOLIA_APP_ID not found in environment variables!`));
        isError = true;
    }
    if (!apiKey) {
        logError(red(`ALGOLIA_WRITE_KEY not found in environment variables!`));
        isError = true;
    }
    if (isError) {
        throw new Error('Make sure environment variables are set');
    }

    return algoliasearch(appId, apiKey);
}

const createDOM = async (pathToHtml: string): Promise<any> => {
    const fileContent = await fs.promises.readFile(pathToHtml, 'utf-8');
    return new JSDOM(fileContent);
};

async function buildPayload(options: HandledRoute): Promise<Payload> {
    const path = join(scullyConfig.outDir, 'docs', options.route, 'index.html');
    const dom = await createDOM(path);
    const { window } = dom;
    const { document } = window;
    const mainTitle = document.querySelector('h1')?.textContent || '';
    const content = getPageContent(document);

    const { data, route } = options;
    const hash = crypto.createHash('sha256');
    const url = route.replace('/', '');
    const category = url.indexOf('/') !== -1 ? url.substring(0, url.indexOf('/')) : url;
    hash.update(route, 'utf8');

    return {
        title: data.title,
        menuTitle: data.displayName,
        mainTitle: mainTitle || data.displayName,
        content,
        url: route,
        product: category,
        objectID: parseInt(hash.digest('hex').slice(0, 15), 16),
    };
}

export const updateAlgoliaIndex = async (routes: Array<HandledRoute>): Promise<void> => {
    if (process.env.BUILD_ENV !== 'develop') {
        try {
            const client = initAlgoliaClient();

            const indexToUse = client.initIndex(INDEX_NAME);

            const indexObjectList = await Promise.all(
                routes.reduce((acc, route) => {
                    if (
                        route.data?.title !== 'metadata' &&
                        route.data?.published &&
                        !route.data?.redirect &&
                        !route.route.startsWith('/reseller-support')
                    ) {
                        return [...acc, buildPayload(route)];
                    }
                    return acc;
                }, []),
            );

            await indexToUse.replaceAllObjects(indexObjectList, { autoGenerateObjectIDIfNotExist: true });

            log(green(`updateAlgolia finished successfully with ${indexObjectList.length} index items`));
        } catch (e) {
            logError('updateAlgolia failed with error', JSON.stringify(e));
            process.exit(1);
        }
    }
};
