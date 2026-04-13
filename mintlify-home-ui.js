/**
 * Homepage: wire [data-mintlify-action] to Mintlify navbar search / Ask AI.
 */
(function () {
  var SEARCH_SELECTORS = [
    "#search-bar-entry",
    "#search-bar-entry-mobile",
    "#navbar #search-bar-entry",
    "#navbar #search-bar-entry-mobile",
    "header #search-bar-entry",
    "header #search-bar-entry-mobile",
    "#navbar .search-bar-entry",
    "#navbar .search-bar-entry-mobile",
    '#navbar [data-component-name="SearchBarEntry"]',
    "button[aria-label*='Search' i]",
  ];
  var ASSISTANT_SELECTORS = [
    "#assistant-entry",
    "#assistant-entry-mobile",
    "#navbar #assistant-entry",
    "#navbar #assistant-entry-mobile",
    "header #assistant-entry",
    "header #assistant-entry-mobile",
    "#navbar .assistant-entry",
    "#navbar .assistant-entry-mobile",
    '#navbar [data-component-name="AssistantEntry"]',
    "button[aria-label*='Ask AI' i]",
  ];
  function triggerClick(selectors) {
    for (var i = 0; i < selectors.length; i++) {
      var el = document.querySelector(selectors[i]);
      if (el) {
        el.click();
        return true;
      }
    }
    return false;
  }
  function dispatchSearchShortcut() {
    var isMac = /Mac|iPhone|iPod|iPad/i.test(navigator.platform || "");
    window.dispatchEvent(
      new KeyboardEvent("keydown", {
        key: "k",
        code: "KeyK",
        bubbles: true,
        cancelable: true,
        metaKey: !!isMac,
        ctrlKey: !isMac,
      })
    );
  }
  function openMintlifySearch() {
    if (!triggerClick(SEARCH_SELECTORS)) dispatchSearchShortcut();
  }
  function openMintlifyAskAI() {
    if (!triggerClick(ASSISTANT_SELECTORS)) openMintlifySearch();
  }
  function setShortcutKbd() {
    var el = document.getElementById("gcore-hero-shortcut-kbd");
    if (el) {
      el.textContent = /Mac|iPhone|iPod|iPad/i.test(navigator.platform || "")
        ? "⌘K"
        : "Ctrl K";
    }
  }
  function onDocClick(e) {
    var s = e.target.closest('[data-mintlify-action="search"]');
    if (s) {
      e.preventDefault();
      e.stopPropagation();
      openMintlifySearch();
      return;
    }
    var a = e.target.closest('[data-mintlify-action="ask-ai"]');
    if (a) {
      e.preventDefault();
      e.stopPropagation();
      openMintlifyAskAI();
    }
  }
  document.addEventListener("click", onDocClick, true);
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setShortcutKbd);
  } else {
    setShortcutKbd();
  }
  window.addEventListener("load", setShortcutKbd);
})();
