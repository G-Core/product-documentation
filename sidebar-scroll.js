(function () {
  'use strict';

  var rafId = null;

  function scrollSidebarToActive() {
    var sidebarContent = document.getElementById('sidebar-content');
    if (!sidebarContent) return;
    var active = sidebarContent.querySelector('li[data-active]');
    if (active) {
      var activeRect = active.getBoundingClientRect();
      var sidebarRect = sidebarContent.getBoundingClientRect();
      // Scroll only the sidebar container, not the page.
      sidebarContent.scrollTop =
        sidebarContent.scrollTop +
        activeRect.top -
        sidebarRect.top -
        sidebarRect.height / 2 +
        activeRect.height / 2;
    }
  }

  // Schedule one scroll per animation frame. Coalesces bursts of mutations
  // (e.g. from React hydration or prefetching) into a single rAF call,
  // without a debounce that would block the scroll until mutations stop.
  function scheduleScroll() {
    if (rafId !== null) return;
    rafId = requestAnimationFrame(function () {
      rafId = null;
      scrollSidebarToActive();
    });
  }

  function attachSidebarObserver(sidebarContent) {
    var observer = new MutationObserver(scheduleScroll);
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
