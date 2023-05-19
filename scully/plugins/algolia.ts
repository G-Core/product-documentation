/* eslint-disable @typescript-eslint/naming-convention */
import crypto from 'crypto';
import { readFileSync } from 'fs';
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

const SETTINGS = undefined;

const INDEX_NAME = 'gcore_site';

export const updateAlgolia = 'updateAlgolia';

const categoriesMap = {
    'account-settings': 'Account settings',
    cdn: 'CDN',
    cloud: 'Cloud',
    dns: 'DNS',
    hosting: 'Hosting',
    storage: 'Storage',
    streaming: 'Streaming',
    'server-protection': 'Server protection',
    'web-security': 'Web security',
    'reseller-support': 'Reseller Support',
};

function initAlgoliaClient(): SearchClient {
    let isError = false;
    const appId = '1U59KUGBCD';
    const apiKey = '7db677961be07c3907096c7eafd0efaa';

    if (!appId) {
        logError(red(`ALGOLIA_APP_ID not found in environment variables!`));
        isError = true;
    }
    if (!apiKey) {
        logError(red(`ALGOLIA_ADMIN_KEY not found in environment variables!`));
        isError = true;
    }
    if (isError) {
        throw new Error('Make sure environment variables are set');
    }

    return algoliasearch(appId, apiKey);
}

function buildPayload(options, mainTitle: string): Payload {
    const { data, route, templateFile } = options;
    const content = readFileSync(templateFile, 'utf8')
        .replace(/---[\S\s]*---/, '')
        .trim();
    const hash = crypto.createHash('sha256');
    const url = route.replace('/documentation/', '');
    const category = url.substr(0, url.indexOf('/'));
    hash.update(data.title, 'utf8');

    return {
        title: data.title,
        menuTitle: data.displayName,
        mainTitle,
        content,
        url: route,
        product: categoriesMap[category],
        objectID: parseInt(hash.digest('hex').slice(0, 15), 16),
    };
}

const updateAlgoliaIndex = async (dom, options): Promise<JSDOM> => {
    try {
        if (options.data.title !== 'metadata') {
            const { window } = dom;
            const { document } = window;
            const mainTitle = document.querySelector('h1')?.innerHTML || '';
            const client = initAlgoliaClient();
            const payload = buildPayload(options, mainTitle);

            const indexToUse = client.initIndex(INDEX_NAME);

            log(`Using [${indexToUse.indexName}]`);

            const { taskID } = await indexToUse.saveObject(payload);
            await indexToUse.waitTask(taskID);

            if (SETTINGS) {
                const { taskID } = await indexToUse.setSettings(SETTINGS);
                await indexToUse.waitTask(taskID);
            }
            log(green(`Updated index for [${payload.title}]`));
        }
    } catch (e) {
        logError(red(JSON.stringify(e, null, 2)));
    }

    return dom;
};

const validator = async (): Promise<Array<any>> => [];

registerPlugin('postProcessByDom', updateAlgolia, updateAlgoliaIndex, validator);
