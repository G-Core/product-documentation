(function () {
  'use strict';

  function scrollSidebarToActive() {
    var sidebarContent = document.getElementById('sidebar-content');
    if (!sidebarContent) return;
    var active = sidebarContent.querySelector('li[data-active]');
    if (active) {
      active.scrollIntoView({ block: 'center', behavior: 'instant' });
    }
  }

  function debounce(fn, ms) {
    var timer = null;
    return function () {
      clearTimeout(timer);
      timer = setTimeout(fn, ms);
    };
  }

  var debouncedScroll = debounce(scrollSidebarToActive, 100);

  function attachSidebarObserver(sidebarContent) {
    var observer = new MutationObserver(debouncedScroll);
    observer.observe(sidebarContent, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ['data-active']
    });
  }

  function init() {
    scrollSidebarToActive();
    var sidebarContent = document.getElementById('sidebar-content');
    if (sidebarContent) {
      attachSidebarObserver(sidebarContent);
    } else {
      var bodyObserver = new MutationObserver(function () {
        var sidebar = document.getElementById('sidebar-content');
        if (sidebar) {
          bodyObserver.disconnect();
          attachSidebarObserver(sidebar);
          scrollSidebarToActive();
        }
      });
      bodyObserver.observe(document.body, { childList: true, subtree: true });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
