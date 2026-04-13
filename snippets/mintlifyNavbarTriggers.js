/** Shared helpers to open Mintlify search / Ask AI from custom UI (navbar ids). */

export function triggerClick(selectors) {
  if (typeof document === "undefined") return false;
  for (const sel of selectors) {
    const el = document.querySelector(sel);
    if (el) {
      el.click();
      return true;
    }
  }
  return false;
}

export function dispatchSearchShortcut() {
  if (typeof window === "undefined" || typeof navigator === "undefined") return;
  const isMac = /Mac|iPhone|iPod|iPad/i.test(navigator.platform || "");
  window.dispatchEvent(
    new KeyboardEvent("keydown", {
      key: "k",
      code: "KeyK",
      bubbles: true,
      cancelable: true,
      ...(isMac ? { metaKey: true } : { ctrlKey: true }),
    })
  );
}

const SEARCH_SELECTORS = [
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

const ASSISTANT_SELECTORS = [
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

export function openMintlifySearch() {
  const opened = triggerClick(SEARCH_SELECTORS);
  if (!opened) dispatchSearchShortcut();
}

export function openMintlifyAskAI() {
  const opened = triggerClick(ASSISTANT_SELECTORS);
  if (!opened) openMintlifySearch();
}
