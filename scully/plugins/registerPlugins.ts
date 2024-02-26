import { registerPlugin } from '@scullyio/scully';
import { updateAlgoliaIndex } from './algolia';
import { moveContent } from './move-content-files/move-content-files';

export const updateAlgolia = 'updateAlgolia';

export const moveContentFiles = 'moveContentFiles';

const validator = async (): Promise<any> => [];

registerPlugin('allDone', moveContentFiles, moveContent, validator);
registerPlugin('allDone', updateAlgolia, updateAlgoliaIndex, validator);
