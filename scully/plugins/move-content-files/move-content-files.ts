import * as path from 'path';
import fs from 'fs-extra';
import { registerPlugin, HandledRoute, scullyConfig, log, green } from '@scullyio/scully';

/* Plugin to move all articles and assets inside docs folder */

type MoveContentFilesPluginOptions = {
    root: string;
    categories: Array<string>;
};

const defaultOptions: Required<MoveContentFilesPluginOptions> = {
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
};
const sitemap = 'sitemap.xml';

export const moveContentFiles = 'moveContentFiles';

async function moveContent(routes: Array<HandledRoute>): Promise<void> {
    const { outDir } = scullyConfig;
    const root = path.join(outDir, defaultOptions.root);

    if (!fs.existsSync(root)) {
        fs.mkdirSync(root);
    }

    defaultOptions.categories.forEach((category) => {
        const categoryPath = path.join(outDir, category);
        if (fs.existsSync(categoryPath)) {
            fs.moveSync(categoryPath, path.join(root, category), { overwrite: true });
        }
    });

    if (fs.existsSync(path.join(outDir, 'search'))) {
        fs.moveSync(path.join(outDir, 'search'), path.join(root, 'search'), { overwrite: true });
    }

    fs.copySync(path.join(outDir, 'index.html'), path.join(root, 'index.html'), { overwrite: true });
    fs.copySync(path.join(outDir, 'assets/scully-routes.json'), path.join(root, 'assets/scully-routes.json'), {
        overwrite: true,
    });

    if (fs.existsSync(path.join(outDir, sitemap))) {
        fs.moveSync(path.join(outDir, sitemap), path.join(root, sitemap), { overwrite: true });
    }

    log(green('MoveContentFiles finished successfully'));
}

const validator = async (): Promise<any> => [];
registerPlugin('allDone', moveContentFiles, moveContent, validator);
