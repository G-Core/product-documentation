import { registerPlugin, HandledRoute } from '@scullyio/scully';
import { JSDOM } from 'jsdom';

const validator = async () => [];

export const copyToClipboardPlugin = 'copyToClipboardPlugin';

const addCopyToClipboardPlugin = async (dom: JSDOM, route: HandledRoute): Promise<JSDOM> => {
    try {
        const { window } = dom;
        const { document } = window;

        const scullyCodeSnippets = document.querySelectorAll('pre>code');
        const copyClipboard = document.querySelectorAll('.gc-copy-to-clipboard');
        const headers = window.document.querySelectorAll('h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]');

        // Copy button for code
        scullyCodeSnippets.forEach((snippet) => {
            snippet = snippet.parentElement;
            const wrapper = document.createElement('div');
            wrapper.style.position = 'relative';
            const copyBtnEl = document.createElement('button');
            copyBtnEl.className = 'gc-copy-to-clipboard';
            copyBtnEl.innerHTML = `
      <span class="tooltip">Copy</span>
      <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M17 7V11C17 13.2091 15.2091 15 13 15V15M17 7V7C17 6.35971 16.7456 5.74565 16.2929 5.29289L12.7071 1.70711C12.2544 1.25435 11.6403 1 11 1V1M17 7H15C12.7909 7 11 5.20914 11 3L11 1M11 1H9C6.79086 1 5 2.79086 5 5V5M13 15L9 15C6.79086 15 5 13.2091 5 11V5M13 15V15C13 17.2091 11.2091 19 9 19H5C2.79086 19 1 17.2091 1 15L1 9C1 6.79086 2.79086 5 5 5V5" stroke="#767283" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    `;
            snippet.prepend(copyBtnEl);
            snippet.parentNode.insertBefore(wrapper, snippet);
            wrapper.appendChild(snippet);
        });

        // Copy link to header
        headers.forEach((header: Element) => {
            header.classList.add('gc-title-with-anchor');
            const anchor = window.document.createElement('button');
            anchor.classList.add('gc-title-anchor-link');
            anchor.dataset.clipboardText = `/docs${route.route}#${header.id}`;
            anchor.setAttribute('title', 'Copy link');
            header.appendChild(anchor);
        });
    } catch (e) {
        console.error(`Error in addCopyToClipboardPlugin plugin: ${e.message}`);
    }
    return dom;
};

registerPlugin('postProcessByDom', copyToClipboardPlugin, addCopyToClipboardPlugin, validator);
