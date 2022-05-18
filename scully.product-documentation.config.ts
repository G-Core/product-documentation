import { RouteConfig, ScullyConfig } from '@scullyio/scully';

/** this loads the default render plugin, remove when switching to something else. */
import '@scullyio/scully-plugin-puppeteer';

const categories = [
  'cdn-dns',
  'video-streaming',
  'cloud-computing',
  'containers',
  'servers',
  'security',
  'cloud-storage',
  'infrastructure',
  'hybrid-cloud',
  'monitoring',
  'custom-services',
];

export const config: ScullyConfig = {
  projectRoot: './src',
  projectName: 'product-documentation',
  // add spsModulePath when using de Scully Platform Server,
  outDir: './dist/static',
  routes: categories.reduce((routes: RouteConfig, category) => {
    routes[`/documentation/${category}/:title`] = {
      type: 'contentFolder',
      title: {
        folder: `./documentation/${category}`,
      },
    };
    return routes;
  }, {}),
};
