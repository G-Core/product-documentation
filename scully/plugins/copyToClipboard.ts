import { registerPlugin, HandledRoute } from '@scullyio/scully';
import { JSDOM } from 'jsdom';
import { __awaiter } from 'tslib';

const validator = async () => [];

export const copyToClipboardPlugin = 'copyToClipboardPlugin';

const addCopyToClipboardPlugin = async (
  dom: JSDOM,
  route: HandledRoute
): Promise<JSDOM> => {
  try {
    // const dom = new JSDOM(html);
    const { window } = dom;
    const { document } = window;

    const scullyCodeSnippets = document.querySelectorAll('pre>code');
    const headers = window.document.querySelectorAll(
      'h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]'
    );

    // Copy button for code
    scullyCodeSnippets.forEach((snippet) => {
      snippet = snippet.parentElement;
      const wrapper = document.createElement('div');
      wrapper.style.position = 'relative';
      const copyBtnEl = document.createElement('button');
      copyBtnEl.className = 'gc-copy-to-clipboard';
      copyBtnEl.textContent = 'Copy';
      snippet.prepend(copyBtnEl);
      snippet.parentNode.insertBefore(wrapper, snippet);
      wrapper.appendChild(snippet);
    });

    // Copy link to header
    headers.forEach((header: Element) => {
      header.classList.add('gc-title-with-anchor');
      const anchor = window.document.createElement('button');
      anchor.classList.add('gc-title-anchor-link');
      anchor.dataset.clipboardText = `${route.route}#${header.id}`;
      anchor.setAttribute('title', 'Copy link');
      header.appendChild(anchor);
    });

    const script = window.document.createElement('script');
    script.defer = true;
    script.async = true;

    script.innerHTML = `
      const s = document.createElement('script');
      s.src = 'assets/clipboard.min.js';
      s.addEventListener('load', () => registerCopyToClipboard());
      s.addEventListener('error', () => console.warn('could not load "assets/clipboard.min.js", make sure you have it copied into your assets folder' ));
      document.body.appendChild(s);

      function registerCopyToClipboard() {
        const clipLink = new ClipboardJS('.gc-title-anchor-link', {
          target: function(trigger) {
            if(!trigger.dataset.clipboardText.startsWith(window.location.origin)) {
              trigger.dataset.clipboardText = window.location.origin + trigger.dataset.clipboardText;
            }
            return trigger;
          }
        });
        clipLink.on('success', function (event) {
          event.trigger.classList.add('gc-anchor-link-copied');
          event.clearSelection();
          setTimeout(function () {
            event.trigger.classList.remove('gc-anchor-link-copied');
          }, 2000);
        });

        const clip = new ClipboardJS('pre .gc-copy-to-clipboard', {
          target: function (trigger) {
            return trigger.nextElementSibling;
          },
        });
        clip.on('success', function (event) {
          event.trigger.textContent = 'Copied!';
          event.clearSelection();
          setTimeout(function () {
            event.trigger.textContent = 'Copy';
          }, 2000);
        });
      }
    `;
    window.document.body.appendChild(script);
  } catch (e) {
    console.error(`Error in anchorLink plugin: ${e.message}`);
  }
  return dom;
};

registerPlugin(
  'postProcessByDom',
  copyToClipboardPlugin,
  addCopyToClipboardPlugin,
  validator
);
