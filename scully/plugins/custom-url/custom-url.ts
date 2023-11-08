import { registerPlugin, HandledRoute } from '@scullyio/scully';

export const setCustomUrls = 'setCustomUrls';

async function setUrls(routes: Array<HandledRoute>): Promise<Array<HandledRoute>> {
    routes.forEach((route) => {
        if (route.data?.customUrl) {
            route.data.originalUrl = route.route;
            route.route = route.data.customUrl;
        }
    });
    return routes;
}

const validator = async (): Promise<any> => [];
registerPlugin('routeProcess', setCustomUrls, setUrls, validator);
