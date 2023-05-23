import { baseHrefRewrite } from '@scullyio/scully-plugin-base-href-rewrite';
import { ScullyConfig, setPluginConfig } from '@scullyio/scully';

/** this loads the default render plugin, remove when switching to something else. */
import '@scullyio/scully-plugin-puppeteer';
import { copyToClipboardPlugin } from './scully/plugins/copyToClipboard';
import { replaceImgSrc } from './scully/plugins/replaceImgSrc';
import { moveContentFiles } from './scully/plugins/move-content-files/move-content-files';
import 'prismjs/components/prism-ruby.min.js';

const baseHref = 'docs';

const defaultPostRenderers = [copyToClipboardPlugin, replaceImgSrc];
setPluginConfig('md', { enableSyntaxHighlighting: true });
setPluginConfig(baseHrefRewrite, { href: baseHref });
setPluginConfig(moveContentFiles, {
    root: baseHref,
    categories: [
        'account-settings',
        'cdn',
        'cloud',
        'dns',
        'hosting',
        'storage',
        'streaming',
        'server-protection',
        'Web security',
        'web-security',
        'Reseller Support',
        'reseller-support',
    ],
});

export const config: ScullyConfig = {
    projectRoot: './src',
    projectName: 'product-documentation',
    outDir: './dist/static',
    defaultPostRenderers: [baseHrefRewrite],
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
