import { registerPlugin } from '@scullyio/scully';
import { JSDOM } from 'jsdom';

const publicUrl = 'http://content-images.s-ed1.cloud.gcore.lu';
const cdnUrl = 'https://assets.gcore.pro';

const validator = async () => [];

export const replaceImgSrc = 'replaceImgSrc';

const replaceSrc = async (dom: JSDOM): Promise<JSDOM> => {
    try {
        const { window } = dom;
        const { document } = window;

        document.querySelectorAll('img').forEach((img) => {
            const src = img.getAttribute('src');
            if (src.startsWith(publicUrl)) {
                img.setAttribute('src', src.replace(publicUrl, cdnUrl));
            }
        });
    } catch (e) {
        console.error(`Error in replaceImgSrc plugin: ${e.message}`);
    }
    return dom;
};

registerPlugin('postProcessByDom', replaceImgSrc, replaceSrc, validator);
