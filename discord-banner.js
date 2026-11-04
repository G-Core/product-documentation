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

  function isHomePage() {
    var path = window.location.pathname.replace(/\/+$/, '') || '/';
    return path === '/' || path === '/home';
  }

  function mount() {
    if (isHomePage()) {
      var homeBanner = document.getElementById(BANNER_ID);
      if (homeBanner) homeBanner.remove();
      return;
    }

    var content = document.querySelector('.mdx-content');
    if (!content || !content.parentElement) return;

    var existing = document.getElementById(BANNER_ID);
    if (existing && !existing.querySelector('.gcore-discord-banner__button')) {
      existing.remove();
      existing = null;
    }
    var toolbar = document.querySelector('.feedback-toolbar');
    if (existing && toolbar && existing.nextElementSibling === toolbar) return;
    if (existing && existing.previousElementSibling === content) return;
    var link = existing || createBanner();
    if (toolbar && toolbar.parentElement) {
      toolbar.parentElement.insertBefore(link, toolbar);
      return;
    }

    content.parentElement.insertBefore(link, content.nextSibling);
  }

  var scheduled = false;

  function schedule() {
    if (scheduled) return;
    scheduled = true;
    window.requestAnimationFrame(function () {
      scheduled = false;
      mount();
    });
  }

  schedule();
  window.addEventListener('mintlify:navigate', schedule);
  if (document.body) {
    new MutationObserver(schedule).observe(document.body, { childList: true, subtree: true });
  }
})();
