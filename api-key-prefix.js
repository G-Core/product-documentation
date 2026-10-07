(function () {
  'use strict';

  // Mintlify renders type:apiKey samples as Authorization: <api-key>.
  // The API requires the APIKey prefix. Re-apply after SPA navigations and
  // after the playground rebuilds a sample.
  var PLACEHOLDER = '<api-key>';
  var REPLACEMENT = 'APIKey <api-key>';
  var PLACEHOLDER_RE = /(?<!APIKey )<api-key>/g;
  var scheduled = false;
  var patching = false;

  function onApiReferencePage() {
    return location.pathname.indexOf('/api-reference/') !== -1;
  }

  function patchTextNode(node) {
    if (!node.nodeValue || node.nodeValue.indexOf(PLACEHOLDER) === -1) return;
    var next = node.nodeValue.replace(PLACEHOLDER_RE, REPLACEMENT);
    if (next !== node.nodeValue) node.nodeValue = next;
  }

  function patchRoot(root) {
    if (!root || !root.querySelectorAll) return;
    var blocks = root.querySelectorAll('pre, code');
    var i;
    var block;
    var walker;
    var textNode;
    for (i = 0; i < blocks.length; i++) {
      block = blocks[i];
      if (block.textContent.indexOf('Authorization') === -1) continue;
      if (block.textContent.indexOf(PLACEHOLDER) === -1) continue;
      walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT, null);
      while ((textNode = walker.nextNode())) patchTextNode(textNode);
    }
  }

  function runPatch() {
    scheduled = false;
    if (!onApiReferencePage()) return;
    patching = true;
    try {
      patchRoot(document.body);
    } finally {
      patching = false;
    }
  }

  function schedulePatch() {
    if (scheduled || patching) return;
    scheduled = true;
    requestAnimationFrame(runPatch);
  }

  var origPushState = history.pushState.bind(history);
  history.pushState = function () {
    origPushState.apply(history, arguments);
    schedulePatch();
  };

  var origReplaceState = history.replaceState.bind(history);
  history.replaceState = function () {
    origReplaceState.apply(history, arguments);
    schedulePatch();
  };

  window.addEventListener('popstate', schedulePatch);

  function init() {
    schedulePatch();
    var observer = new MutationObserver(function () {
      if (!patching) schedulePatch();
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
