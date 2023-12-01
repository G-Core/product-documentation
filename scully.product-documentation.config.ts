import { ScullyConfig, setPluginConfig } from '@scullyio/scully';

/** this loads the default render plugin, remove when switching to something else. */
import '@scullyio/scully-plugin-puppeteer';
import { copyToClipboardPlugin } from './scully/plugins/copyToClipboard';
import { replaceImgSrc } from './scully/plugins/replaceImgSrc';
import 'prismjs/components/prism-ruby.min.js';
import { updateAlgolia } from './scully/plugins/algolia';
import { getSitemapPlugin } from './scully/plugins/sitemap';
require('dotenv').config()

const categories = [
    'web-security',
    'streaming',
    'server-protection',
    'storage',
    'hosting',
    'dns',
    'cloud',
    'cdn',
    'account-settings',
    'reseller-support',
];
import { moveContentFiles } from './scully/plugins/move-content-files/move-content-files';
import { setCustomUrls } from './scully/plugins/custom-url/custom-url';

const SitemapPlugin = getSitemapPlugin();

const defaultPostRenderers = [updateAlgolia, copyToClipboardPlugin, replaceImgSrc];
setPluginConfig('md', { enableSyntaxHighlighting: true });
setPluginConfig(moveContentFiles, {
    root: 'docs',
    categories: [
        'account-settings',
        'cdn',
        'cloud',
        'dns',
        'hosting',
        'storage',
        'streaming-platform',
        'ddos-protection',
        'web-security',
        'reseller-support',
    ],
});
setPluginConfig(SitemapPlugin, {
    urlPrefix: 'https://gcore.com/docs',
    sitemapFilename: 'sitemap.xml',
    ignoredRoutes: [],
    ignoredRoutesPattern: [/\/metadata$/, /___UNPUBLISHED___/],
    merge: false,
    trailingSlash: false,
    changeFreq: 'monthly',
    priority: ['1.0', '0.9', '0.8', '0.7', '0.6', '0.5', '0.4', '0.3', '0.2', '0.1', '0.0'],
});
setPluginConfig(setCustomUrls, {});



export const config: ScullyConfig = {
    projectRoot: './src',
    projectName: 'product-documentation',
    outDir: './dist/static',
    distFolder: './dist/product-documentation',
    puppeteerLaunchOptions:
        process.env.BUILD_ENV === 'develop'
            ? undefined
            : {
                  executablePath: process.env.CHROME_PATH || '/usr/bin/chromium-browser',
                  args: ['--no-sandbox'],
              },
    routes: {
        // eslint-disable-next-line @typescript-eslint/naming-convention
        '/:title': {
            type: 'contentFolder',
            postRenderers: defaultPostRenderers,
            title: {
                folder: `./documentation`,
            },
        },
    },
};
