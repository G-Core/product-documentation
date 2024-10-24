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
        name: 'Edge Cloud',
        url: 'cloud',
    },
    {
        name: 'Managed DNS',
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
        name: 'Video Streaming',
        url: 'streaming-platform',
    },
    {
        name: 'DDoS Protection',
        url: 'ddos-protection',
    },
    {
        name: 'WAAP',
        url: 'waap',
    },
    {
        name: 'Reseller Support',
        url: 'reseller-support',
    },
    {
        name: 'Edit article guide',
        url: 'edit-article-guide',
    },
    {
        name: 'Edge AI',
        url: 'edge-ai',
    },
];
