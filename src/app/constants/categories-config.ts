import { Category } from '../models';

// Adding or updating categories requires the same changes to categoriesMap in scully/plugins/algolia
export const categories: Array<Category> = [
    {
        name: 'Account settings',
        url: 'account-settings',
    },
    {
        name: 'CDN',
        url: 'cdn',
    },
    {
        name: 'Cloud',
        url: 'cloud',
    },
    {
        name: 'DNS',
        url: 'dns',
    },
    {
        name: 'Hosting',
        url: 'hosting',
    },
    {
        name: 'Storage',
        url: 'storage',
    },
    {
        name: 'Streaming',
        url: 'streaming',
    },
    {
        name: 'Server protection',
        url: 'server-protection',
    },
    {
        name: 'Web security',
        url: 'web-security',
    },
    {
        name: 'Reseller Support',
        url: 'reseller-support',
    },
];
