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
      var activeRect = active.getBoundingClientRect();
      var sidebarRect = sidebarContent.getBoundingClientRect();
      // Scroll only the sidebar container, not the page.
      sidebarContent.scrollTop =
        sidebarContent.scrollTop +
        activeRect.top -
        sidebarRect.top -
        sidebarRect.height / 2 +
        activeRect.height / 2;
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

  // Ensure only one rAF loop runs at a time. Extend the polling window on each call.
  function startPolling() {
    pollDeadline = Date.now() + POLL_DURATION_MS;
    if (rafId === null) {
      rafId = requestAnimationFrame(poll);
    }
  }

  // Intercept Next.js pushState so we detect SPA navigation the moment it starts.
  // This is more reliable than MutationObserver alone because Mintlify may replace
  // the entire #sidebar-content element on navigation, detaching any observer on it.
  var origPushState = history.pushState.bind(history);
  history.pushState = function () {
    origPushState.apply(history, arguments);
    startPolling();
  };
  window.addEventListener('popstate', startPolling);

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
