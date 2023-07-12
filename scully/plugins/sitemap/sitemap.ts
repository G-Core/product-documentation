import * as fs from 'fs';
import * as path from 'path';
import * as builder from 'xmlbuilder';
import { pathToRegexp } from 'path-to-regexp';
import { XMLParser } from 'fast-xml-parser';
import { registerPlugin, HandledRoute, scullyConfig, getPluginConfig } from '@scullyio/scully';
import { SitemapConfig, defaultSitemapConfig } from './sitemap-config';

const today = new Date();
const SitemapPlugin = 'sitemap';

const mergePaths = (base: string, path: string): string => {
    if (base.endsWith('/') && path.startsWith('/')) {
        return `${base}${path.substr(1)}`;
    }
    if (!base.endsWith('/') && !path.startsWith('/')) {
        return `${base}/${path}`;
    }
    return `${base}${path}`;
};

const priorityForLocation = (loc: string, config: SitemapConfig): string => {
    if (typeof config.priority === 'string' || config.priority instanceof String) {
        return config.priority as string;
    } else if (Array.isArray(config.priority)) {
        const segments = loc.split('/');
        return config.priority[segments.length - 1];
    } else {
        return '0.5';
    }
};

const pluralizer = (num: number, singular: string, plural: string): string => {
    return num === 1 ? singular : plural;
};

const configForRoute = (config: SitemapConfig, route: HandledRoute): any => {
    if (config.routes) {
        // tslint:disable-next-line: forin
        for (const routePath in config.routes) {
            const routeConfig = config.routes[routePath];
            if (route.route.match(routeConfig.regexp)) {
                return {
                    route: route.route,
                    urlPrefix: routeConfig.urlPrefix || config.urlPrefix,
                    trailingSlash: routeConfig.trailingSlash || config.trailingSlash,
                    sitemapFilename: routeConfig.sitemapFilename || config.sitemapFilename,
                    merge: routeConfig.merge || config.merge,
                    changeFreq: routeConfig.changeFreq || config.changeFreq,
                    priority: routeConfig.priority || config.priority,
                };
            }
        }
    }
    return {
        route: route.route,
        urlPrefix: config.urlPrefix,
        trailingSlash: config.trailingSlash,
        sitemapFilename: config.sitemapFilename,
        merge: config.merge,
        changeFreq: config.changeFreq,
        priority: config.priority,
    };
};

const getSitemapFile = (filename: string): string => {
    return path.join(scullyConfig.outDir, filename);
};

const parseXml = (xmlString): string => {
    const xmlParser = new XMLParser();
    return xmlParser.parse(xmlString);
};

const loadMap = (filename: string): any => {
    const file = getSitemapFile(filename);
    if (fs.existsSync(file)) {
        const xmlString = fs.readFileSync(file, { encoding: 'utf8', flag: 'r' });
        const xml = parseXml(xmlString) as any;
        // build url object
        const map = {};
        for (const mappedUrl of xml.urlset.url) {
            map[mappedUrl.loc] = mappedUrl;
        }
        return map;
    } else {
        return null;
    }
};

const saveMap = (map, filename): builder.XMLElement => {
    const file = getSitemapFile(filename);
    const rootElement = builder.create('urlset').att('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9');
    for (const route of Object.values(map) as Array<any>) {
        const urlElement = rootElement.ele('url');
        urlElement.ele('loc', route.loc);
        urlElement.ele('changefreq', route.changefreq);
        urlElement.ele('lastmod', route.lastmod);
        urlElement.ele('priority', route.priority);
    }
    const xml = rootElement.end({ pretty: true });
    fs.writeFileSync(file, xml);
    return rootElement;
};

const getMapForRoute = (maps: any, routeConfig: any): any => {
    let map = maps[routeConfig.sitemapFilename];
    if (!map && routeConfig.merge) {
        map = loadMap(routeConfig.sitemapFilename);
    }
    if (!map) {
        map = {};
    }
    maps[routeConfig.sitemapFilename] = map;
    return map;
};

export const sitemapPlugin = async (routes: Array<HandledRoute>): Promise<void> => {
    const config = { ...defaultSitemapConfig, ...(getPluginConfig(SitemapPlugin) as SitemapConfig) };

    const log = (message?: any, ...optionalParams: Array<any>): void => {
        if (!config.suppressLog) {
            console.log(message, ...optionalParams);
        }
    };

    log(`Started scully-plugin-sitemap`);
    log(`Generating sitemaps for ${routes.length} ${pluralizer(routes.length, 'route', 'routes')}.`);

    // parse route configurations
    if (config.routes) {
        Object.keys(config.routes).forEach((key) => {
            config.routes[key].regexp = pathToRegexp(key);
        });
    }

    const maps = {};

    routes.forEach((route: HandledRoute) => {
        if (
            config.ignoredRoutes &&
            (config.ignoredRoutes.includes(route.route) ||
                config.ignoredRoutesPattern.some((regExp) => regExp.test(route.route)))
        ) {
            return;
        }
        const routeConfig = configForRoute(config, route);
        const map = getMapForRoute(maps, routeConfig);
        let loc = mergePaths(routeConfig.urlPrefix, route.route);
        if (routeConfig.trailingSlash && !loc.endsWith('/')) {
            loc = `${loc}/`;
        }
        map[loc] = {
            loc,
            changefreq: routeConfig.changeFreq,
            lastmod: today.toISOString(),
            priority: priorityForLocation(route.route, routeConfig),
        };
    });

    // tslint:disable-next-line: forin
    for (const filename in maps) {
        const rootElement = saveMap(maps[filename], filename);
        const routeCount = rootElement.children.length;
        log(`Wrote ${routeCount} ${pluralizer(routeCount, 'route', 'routes')} to ${filename}`);
    }

    log(`Finished scully-plugin-sitemap`);
};

const validator = async (conf): Promise<Array<any>> => [];
registerPlugin('routeDiscoveryDone', SitemapPlugin, sitemapPlugin, validator);

export const getSitemapPlugin = (): string => SitemapPlugin;
