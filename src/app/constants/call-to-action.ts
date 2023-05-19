/* eslint-disable sonarjs/no-duplicate-string */
/* eslint-disable @typescript-eslint/naming-convention */
import { CallToActionBoxContent } from '../ui-kit/call-to-action-box/call-to-action-box-content';

export const callToActionMap: { [key: string]: CallToActionBoxContent } = {
    cdn: {
        title: 'Not a Gcore user yet?',
        description: 'Learn more about our next-gen CDN',
        buttonLabel: 'Go to the product page',
        url: 'https://gcore.com/cdn',
    },
    cloud: {
        title: 'Not a Gcore user yet?',
        description:
            'Discover our offerings, including virtual instances starting from 3.7 euro/mo, bare metal servers, AI Infrastructure, load balancers, Managed Kubernetes, Function as a Service, and Centralized Logging solutions.',
        buttonLabel: 'Go to the product page',
        url: 'https://gcore.com/cloud',
    },
    dns: {
        title: 'Not a Gcore user yet?',
        description: 'Learn more about our DNS hosting',
        buttonLabel: 'Go to the product page',
        url: 'https://gcore.com/dns',
    },
    hosting: {
        title: 'Not a Gcore user yet?',
        description: 'Enhance your online presence with our virtual and dedicated servers.',
        buttonLabel: 'Go to the product page',
        url: 'https://gcore.com/hosting',
    },
    streaming: {
        title: 'Not a Gcore user yet?',
        description: 'Explore the Streaming Platform by Gcore',
        buttonLabel: 'Go to the product page',
        url: 'https://gcore.com/streaming-platform',
    },
    'server-protection': {
        title: 'Not a Gcore user yet?',
        description: 'Explore our DDoS protection for servers',
        buttonLabel: 'Go to the product page',
        url: 'https://gcore.com/ddos-protection',
    },
    storage: {
        title: 'Not a Gcore user yet?',
        description: 'Check out our Storage',
        buttonLabel: 'Go to the product page',
        url: 'https://gcore.com/storage',
    },
    'web-security': {
        title: 'Not a Gcore user yet?',
        description: 'Discover the all-in-one Web security solution by Gcore',
        buttonLabel: 'Go to the product page',
        url: 'https://gcore.com/web-security',
    },
};
