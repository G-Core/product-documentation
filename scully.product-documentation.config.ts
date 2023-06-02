import { ScullyConfig, setPluginConfig } from '@scullyio/scully';

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
import { moveContentFiles } from './scully/plugins/move-content-files/move-content-files';

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

export const config: ScullyConfig = {
    projectRoot: './src',
    projectName: 'product-documentation',
    outDir: './dist/static',
    distFolder: './dist/product-documentation',
    puppeteerLaunchOptions:
        process.env.BUILD_ENV === 'develop'
            ? undefined
            : {
                  executablePath: '/usr/bin/chromium-browser',
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
