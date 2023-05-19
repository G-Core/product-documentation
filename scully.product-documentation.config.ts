import { RouteConfig, ScullyConfig, setPluginConfig } from '@scullyio/scully';

/** this loads the default render plugin, remove when switching to something else. */
import '@scullyio/scully-plugin-puppeteer';
import { copyToClipboardPlugin } from './scully/plugins/copyToClipboard';
import { replaceImgSrc } from './scully/plugins/replaceImgSrc';
import 'prismjs/components/prism-ruby.min.js';
import { updateAlgolia } from './scully/plugins/algolia';

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

const defaultPostRenderers = [updateAlgolia, copyToClipboardPlugin, replaceImgSrc];
setPluginConfig('md', { enableSyntaxHighlighting: true });

export const config: ScullyConfig = {
    projectRoot: './src',
    projectName: 'product-documentation',
    outDir: './dist/static',
    puppeteerLaunchOptions:
        process.env.BUILD_ENV === 'develop'
            ? undefined
            : {
                  executablePath: '/usr/bin/chromium-browser',
                  args: ['--no-sandbox'],
              },
    routes: categories.reduce((routes: RouteConfig, category) => {
        routes[`/documentation/${category}/:title`] = {
            type: 'contentFolder',
            postRenderers: defaultPostRenderers,
            title: {
                folder: `./documentation/${category}`,
            },
        };
        return routes;
    }, {}),
};
