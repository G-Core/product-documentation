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
        name: 'FastEdge',
        url: 'fastedge',
    },
    {
        name: 'Cloud',
        url: 'cloud',
    },
    {
        name: 'DNS Hosting',
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
        name: 'Streaming platform',
        url: 'streaming-platform',
    },
    {
        name: 'DDoS protection',
        url: 'ddos-protection',
    },
    {
        name: 'Web security',
        url: 'web-security',
    },
    {
        name: 'Reseller Support',
        url: 'reseller-support',
    },
    {
        name: 'Edit article guide',
        url: 'edit-article-guide',
    },
];
