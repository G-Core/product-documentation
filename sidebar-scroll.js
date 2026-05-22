(function () {
  'use strict';

  var POLL_DURATION_MS = 2000;
  var rafId = null;
  var pollDeadline = 0;

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

  function poll() {
    rafId = null;
    if (scrollSidebarToActive()) return;
    if (Date.now() < pollDeadline) {
      rafId = requestAnimationFrame(poll);
    }
  }

  // Extend the polling window and ensure exactly one rAF loop is running.
  function startPolling() {
    pollDeadline = Date.now() + POLL_DURATION_MS;
    if (rafId === null) {
      rafId = requestAnimationFrame(poll);
    }
  }

  function attachSidebarObserver(sidebarContent) {
    var observer = new MutationObserver(startPolling);
    observer.observe(sidebarContent, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ['data-active']
    });
  }

  function init() {
    startPolling();
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
