"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.config = void 0;
const scully_1 = require("@scullyio/scully");
/** this loads the default render plugin, remove when switching to something else. */
require("@scullyio/scully-plugin-puppeteer");
const copyToClipboard_1 = require("./scully/plugins/copyToClipboard");
const replaceImgSrc_1 = require("./scully/plugins/replaceImgSrc");
require("prismjs/components/prism-ruby.min.js");
const categories = [
    'cdn-dns',
    'video-streaming',
    'cloud-computing',
    'containers',
    'services',
    'security',
    'cloud-storage',
    'infrastructure',
    'hybrid-cloud',
    'monitoring',
    'custom-services',
];
const defaultPostRenderers = [copyToClipboard_1.copyToClipboardPlugin, replaceImgSrc_1.replaceImgSrc];
(0, scully_1.setPluginConfig)('md', { enableSyntaxHighlighting: true });
exports.config = {
    projectRoot: './src',
    projectName: 'product-documentation',
    outDir: './dist/static',
    puppeteerLaunchOptions: process.env.BUILD_ENV === 'develop'
        ? undefined
        : {
            executablePath: '/usr/bin/chromium-browser',
            args: ['--no-sandbox'],
        },
    routes: categories.reduce((routes, category) => {
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
