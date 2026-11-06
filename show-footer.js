(function () {
  'use strict';

  // Home is a custom page. Mintlify hides #footer there with a layered
  // !important rule that a stylesheet cannot override. An inline important
  // style can. The same footer stays visible on every other page.
  function showFooter() {
    var footer = document.getElementById('footer');
    if (!footer) return;
    if (footer.style.getPropertyPriority('display') === 'important') return;
    footer.style.setProperty('display', 'flex', 'important');
  }

  function start() {
    showFooter();
    var root = document.body;
    if (!root || root.dataset.footerObserver === '1') return;
    root.dataset.footerObserver = '1';
    new MutationObserver(showFooter).observe(root, {
      childList: true,
      subtree: true
    });
  }

  if (document.body) {
    start();
  } else {
    document.addEventListener('DOMContentLoaded', start);
  }
})();
