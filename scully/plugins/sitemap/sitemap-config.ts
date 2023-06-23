/* eslint-disable max-classes-per-file */
/**
 * The sitemap configuration options.
 */
export class SitemapRoute {
    /** The path RegExp (automatically generated) */
    public regexp?: RegExp;

    /** What is the base url to your app. */
    public urlPrefix?: string;

    /** How often is the route expected to change? */
    public changeFreq?: 'always' | 'hourly' | 'daily' | 'weekly' | 'monthly' | 'yearly';

    /** Where do you want to store the sitemap file? */
    public sitemapFilename?: string;

    /** Merge handled routes into existing sitemap file (if available)? */
    public merge?: boolean;

    /** A list of priorities to set based on number of segments in the route */
    public priority?: string | Array<string>;

    /** would you like to append a trailing slash to the url */
    public trailingSlash?: boolean;
}

/**
 * The sitemap configuration options.
 */
export class SitemapConfig {
    /** What is the base url to your app. */
    public urlPrefix: string;

    /** Where do you want to store the sitemap file? */
    public sitemapFilename: string;

    /** Merge handled routes into existing sitemap file (if available)? */
    public merge?: boolean;

    /** How often is the route expected to change? */
    public changeFreq?: 'always' | 'hourly' | 'daily' | 'weekly' | 'monthly' | 'yearly';

    /** A list of priorities to set based on number of segments in the route */
    public priority?: string | Array<string>;

    /** A list of routes not to include in the sitemap */
    public ignoredRoutes?: Array<string>;

    /** A list of route patterns not to include in the sitemap */
    public ignoredRoutesPattern?: Array<RegExp>;

    /** If `true`, the plugin will not log status messages to the console. */
    public suppressLog?: boolean;

    /** List of optional configuration for specific routes */
    public routes?: { [route: string]: SitemapRoute };

    /** would you like to append a trailing slash to the url */
    public trailingSlash?: boolean;
}

/**
 * The default configuration
 */
export const defaultSitemapConfig: SitemapConfig = {
    urlPrefix: 'http://localhost',
    sitemapFilename: 'sitemap.xml',
    merge: false,
    changeFreq: 'monthly',
    priority: '0.5',
    suppressLog: false,
    trailingSlash: false,
};
