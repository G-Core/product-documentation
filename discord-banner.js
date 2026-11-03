(function () {
  'use strict';

  var BANNER_ID = 'gcore-discord-banner';
  var IMAGE_SRC = '/images/docs/discord-banner/join-discord.svg?v=2';
  var LINK_HREF = 'https://discord.gg/gcore';

  function createBanner() {
    var banner = document.createElement('div');
    banner.id = BANNER_ID;
    banner.className = 'gcore-discord-banner';

    var image = document.createElement('img');
    image.src = IMAGE_SRC;
    image.alt = '';
    image.setAttribute('aria-hidden', 'true');
    banner.appendChild(image);

    var button = document.createElement('a');
    button.className = 'gcore-discord-banner__button';
    button.href = LINK_HREF;
    button.target = '_blank';
    button.rel = 'noopener noreferrer';
    button.textContent = 'Join Gcore Discord';
    banner.appendChild(button);
    return banner;
  }

  function mount() {
    var content = document.querySelector('.mdx-content');
    if (!content || !content.parentElement) return;

    var existing = document.getElementById(BANNER_ID);
    if (existing && !existing.querySelector('.gcore-discord-banner__button')) {
      existing.remove();
      existing = null;
    }
    var link = existing || createBanner();
    var toolbar = document.querySelector('.feedback-toolbar');
    if (toolbar && toolbar.parentElement) {
      toolbar.parentElement.insertBefore(link, toolbar);
      return;
    }

    content.parentElement.insertBefore(link, content.nextSibling);
  }

  function schedule() {
    mount();
    window.requestAnimationFrame(mount);
    window.setTimeout(mount, 50);
    window.setTimeout(mount, 300);
  }

  schedule();
  window.addEventListener('mintlify:navigate', schedule);
})();
