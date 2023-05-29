import * as path from 'path';
import fs from 'fs-extra';
import { registerPlugin, HandledRoute, scullyConfig, log, green } from '@scullyio/scully';

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
        'streaming',
        'server-protection',
        'Web security',
        'web-security',
        'Reseller Support',
        'reseller-support',
    ],
};

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

    fs.copySync(path.join(outDir, 'index.html'), path.join(root, 'index.html'), { overwrite: true });

    log(green('MoveContentFiles finished successfully'));
}

const validator = async (): Promise<any> => [];
registerPlugin('allDone', moveContentFiles, moveContent, validator);
