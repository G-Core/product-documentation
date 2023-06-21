/* eslint-disable @typescript-eslint/naming-convention */
import crypto from 'crypto';
import { registerPlugin, log, green, red, logError } from '@scullyio/scully';
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

export const updateAlgolia = 'updateAlgolia';

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

    console.log('APP ID:', appId);
    console.log('APP INDEX_NAME:', INDEX_NAME);

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

function buildPayload(options, mainTitle: string, content: string): Payload {
    const { data, route } = options;
    const hash = crypto.createHash('sha256');
    const url = route.replace('/', '');
    const category = url.indexOf('/') !== -1 ? url.substr(0, url.indexOf('/')) : url;
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

const updateAlgoliaIndex = async (dom, options): Promise<JSDOM> => {
    if (process.env.BUILD_ENV === 'develop' || options.route.startsWith('/reseller-support')) {
        return dom;
    }
    try {
        if (options.data.title !== 'metadata') {
            const { window } = dom;
            const { document } = window;
            const mainTitle = document.querySelector('h1')?.innerHTML || '';
            const content = getPageContent(document);
            const client = initAlgoliaClient();
            const payload = buildPayload(options, mainTitle, content);

            const indexToUse = client.initIndex(INDEX_NAME);

            log(`Using [${indexToUse.indexName}]`);

            const { taskID } = await indexToUse.saveObject(payload);
            await indexToUse.waitTask(taskID);

            log(green(`Updated index for [${payload.title}]`));
        }
    } catch (e) {
        logError(red(JSON.stringify(e, null, 2)));
    }

    return dom;
};

const validator = async (): Promise<Array<any>> => [];

registerPlugin('postProcessByDom', updateAlgolia, updateAlgoliaIndex, validator);
