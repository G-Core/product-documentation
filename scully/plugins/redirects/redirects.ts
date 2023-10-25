import * as path from 'path';
import fs from 'fs-extra';
import { registerPlugin, HandledRoute, scullyConfig } from '@scullyio/scully';

export const setOldUrlsRedirects = 'setOldUrlsRedirects';

async function setRedirects(routes: Array<HandledRoute>): Promise<void> {
    const { homeFolder } = scullyConfig;
    const configPath = path.join(homeFolder, 'default.conf');
    const redirectedRoutes = routes.filter((route) => route.data?.oldUrl);
    const redirectString = redirectedRoutes
        .map(
            (route) =>
                `location ~ ^/docs${route.data.oldUrl as string}/?$ { return 301 https://$host/docs${route.route}; }`,
        )
        .join('\n    ');
    const config = fs.readFileSync(configPath, {
        encoding: 'utf8',
    });
    const updatedConfig = config.replace('###REDIRECTS###', redirectString);
    fs.writeFileSync(configPath, updatedConfig);
}

const validator = async (): Promise<any> => [];
registerPlugin('allDone', setOldUrlsRedirects, setRedirects, validator);
