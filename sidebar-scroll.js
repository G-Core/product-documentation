(function () {
  'use strict';

  var POLL_DURATION_MS = 2000;

  function scrollSidebarToActive() {
    var sidebarContent = document.getElementById('sidebar-content');
    if (!sidebarContent) return false;
    var active = sidebarContent.querySelector('li[data-active]');
    if (active) {
      active.scrollIntoView({ block: 'center', behavior: 'instant' });
      return true;
    }
    return false;
  }

  // Poll every animation frame until the active item appears or the deadline passes.
  // This catches data-active as soon as React hydration sets it, without waiting for
  // an arbitrary debounce delay.
  function pollUntilActive(deadline) {
    if (scrollSidebarToActive()) return;
    if (Date.now() < deadline) {
      requestAnimationFrame(function () { pollUntilActive(deadline); });
    }
  }

  function attachSidebarObserver(sidebarContent) {
    var observer = new MutationObserver(function () {
      // Restart polling on every sidebar mutation so SPA navigations are handled
      // with the same low-latency approach as initial load.
      pollUntilActive(Date.now() + POLL_DURATION_MS);
    });
    observer.observe(sidebarContent, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ['data-active']
    });
  }

  function init() {
    pollUntilActive(Date.now() + POLL_DURATION_MS);

    var sidebarContent = document.getElementById('sidebar-content');
    if (sidebarContent) {
      attachSidebarObserver(sidebarContent);
    } else {
      var bodyObserver = new MutationObserver(function () {
        var sidebar = document.getElementById('sidebar-content');
        if (sidebar) {
          bodyObserver.disconnect();
          attachSidebarObserver(sidebar);
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
