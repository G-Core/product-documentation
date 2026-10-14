(function () {
  'use strict';

  var PROMPT =
    'Fetch and execute the appropriate instructions to set me up for FastEdge from https://portal.gcore.com/external-statics/fast-edge/agent-connect-prompt.md';

  var AGENTS = [
    {
      id: 'claude',
      label: 'Claude Code',
      svg: '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m4.7144 15.9555 4.7174-2.6471.079-.2307-.079-.1275h-.2307l-.7893-.0486-2.6956-.0729-2.3375-.0971-2.2646-.1214-.5707-.1215-.5343-.7042.0546-.3522.4797-.3218.686.0608 1.5179.1032 2.2767.1578 1.6514.0972 2.4468.255h.3886l.0546-.1579-.1336-.0971-.1032-.0972L6.973 9.8356l-2.55-1.6879-1.3356-.9714-.7225-.4918-.3643-.4614-.1578-1.0078.6557-.7225.8803.0607.2246.0607.8925.686 1.9064 1.4754 2.4893 1.8336.3643.3035.1457-.1032.0182-.0728-.164-.2733-1.3539-2.4467-1.445-2.4893-.6435-1.032-.17-.6194c-.0607-.255-.1032-.4674-.1032-.7285L6.287.1335 6.6997 0l.9957.1336.419.3642.6192 1.4147 1.0018 2.2282 1.5543 3.0296.4553.8985.2429.8318.091.255h.1579v-.1457l.1275-1.706.2368-2.0947.2307-2.6957.0789-.7589.3764-.9107.7468-.4918.5828.2793.4797.686-.0668.4433-.2853 1.8517-.5586 2.9021-.3643 1.9429h.2125l.2429-.2429.9835-1.3053 1.6514-2.0643.7286-.8196.85-.9046.5464-.4311h1.0321l.759 1.1293-.34 1.1657-1.0625 1.3478-.8804 1.1414-1.2628 1.7-.7893 1.36.0729.1093.1882-.0183 2.8535-.607 1.5421-.2794 1.8396-.3157.8318.3886.091.3946-.3278.8075-1.967.4857-2.3072.4614-3.4364.8136-.0425.0304.0486.0607 1.5482.1457.6618.0364h1.621l3.0175.2247.7892.522.4736.6376-.079.4857-1.2142.6193-1.6393-.3886-3.825-.9107-1.3113-.3279h-.1822v.1093l1.0929 1.0686 2.0035 1.8092 2.5075 2.3314.1275.5768-.3218.4554-.34-.0486-2.2039-1.6575-.85-.7468-1.9246-1.621h-.1275v.17l.4432.6496 2.3436 3.5214.1214 1.0807-.17.3521-.6071.2125-.6679-.1214-1.3721-1.9246L14.38 17.959l-1.1414-1.9428-.1397.079-.674 7.2552-.3156.3703-.7286.2793-.6071-.4614-.3218-.7468.3218-1.4753.3886-1.9246.3157-1.53.2853-1.9004.17-.6314-.0121-.0425-.1397.0182-1.4328 1.9672-2.1796 2.9446-1.7243 1.8456-.4128.164-.7164-.3704.0667-.6618.4008-.5889 2.386-3.0357 1.4389-1.882.929-1.0868-.0062-.1579h-.0546l-6.3385 4.1164-1.1293.1457-.4857-.4554.0608-.7467.2307-.2429 1.9064-1.3114Z"></path></svg>'
    },
    {
      id: 'codex',
      label: 'Codex',
      svg: '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"></path></svg>'
    },
    {
      id: 'cursor',
      label: 'Cursor',
      svg: '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M11.503.131 1.891 5.678a.84.84 0 0 0-.42.726v11.188c0 .3.162.575.42.724l9.609 5.55a1 1 0 0 0 .998 0l9.61-5.55a.84.84 0 0 0 .42-.724V6.404a.84.84 0 0 0-.42-.726L12.497.131a1.01 1.01 0 0 0-.996 0M2.657 6.338h18.55c.263 0 .43.287.297.515L12.23 22.918c-.062.107-.229.064-.229-.06V12.335a.59.59 0 0 0-.295-.51l-9.11-5.257c-.109-.063-.064-.23.061-.23"></path></svg>'
    },
    {
      id: 'other',
      label: 'Other agents',
      svg: '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.85 0a4.16 4.16 0 0 0-2.95 1.217L1.456 10.66a.835.835 0 0 0 0 1.18.835.835 0 0 0 1.18 0l9.442-9.442a2.49 2.49 0 0 1 3.541 0 2.49 2.49 0 0 1 0 3.541L8.59 12.97l-.1.1a.835.835 0 0 0 0 1.18.835.835 0 0 0 1.18 0l.1-.098 7.03-7.034a2.49 2.49 0 0 1 3.542 0l.049.05a2.49 2.49 0 0 1 0 3.54l-8.54 8.54a1.96 1.96 0 0 0 0 2.755l1.753 1.753a.835.835 0 0 0 1.18 0 .835.835 0 0 0 0-1.18l-1.753-1.753a.266.266 0 0 1 0-.394l8.54-8.54a4.185 4.185 0 0 0 0-5.9l-.05-.05a4.16 4.16 0 0 0-2.95-1.218c-.2 0-.401.02-.6.048a4.17 4.17 0 0 0-1.17-3.552A4.16 4.16 0 0 0 13.85 0m0 3.333a.84.84 0 0 0-.59.245L6.275 10.56a4.186 4.186 0 0 0 0 5.902 4.186 4.186 0 0 0 5.902 0L19.16 9.48a.835.835 0 0 0 0-1.18.835.835 0 0 0-1.18 0l-6.985 6.984a2.49 2.49 0 0 1-3.54 0 2.49 2.49 0 0 1 0-3.54l6.983-6.985a.835.835 0 0 0 0-1.18.84.84 0 0 0-.59-.245"></path></svg>'
    },
    {
      id: 'vscode',
      label: 'VS Code',
      svg: '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M17 2l5 2.4v15.2L17 22 7.5 13.3 3.4 16.4 2 15.7V8.3l1.4-.7 4.1 3.1zM17 7.2L10.7 12l6.3 4.8z"></path></svg>'
    }
  ];

  var copiedTimer = null;
  var tip = null;
  var TIP_WIDTH = 200;

  function tooltipEl() {
    if (tip) return tip;
    tip = document.createElement('div');
    tip.className = 'fastedge-agent-setup-tip';
    tip.setAttribute('role', 'tooltip');
    tip.hidden = true;
    document.body.appendChild(tip);
    window.addEventListener('scroll', hideTip, true);
    window.addEventListener('resize', hideTip);
    return tip;
  }

  function hideTip() {
    if (!tip) return;
    tip.hidden = true;
    tip.classList.remove('is-compact');
  }

  function showTip(anchor, text) {
    var node = tooltipEl();
    node.textContent = text;
    node.hidden = false;
    var rect = anchor.getBoundingClientRect();
    var margin = 8;
    var width = node.classList.contains('is-compact') ? node.offsetWidth : TIP_WIDTH;
    var left = node.classList.contains('is-compact')
      ? rect.left + (rect.width - width) / 2
      : rect.left;
    if (left + width > window.innerWidth - margin) {
      left = window.innerWidth - width - margin;
    }
    if (left < margin) left = margin;
    node.style.left = left + 'px';
    var height = node.offsetHeight;
    var top = rect.bottom + 6;
    if (top + height > window.innerHeight - margin && rect.top > height + margin) {
      top = rect.top - height - 6;
    }
    node.style.top = top + 'px';
  }

  function bindTip(anchor, text) {
    anchor.addEventListener('mouseenter', function () { showTip(anchor, text); });
    anchor.addEventListener('mouseleave', hideTip);
    anchor.addEventListener('focus', function () { showTip(anchor, text); });
    anchor.addEventListener('blur', hideTip);
  }

  function isFastedge(path) {
    return path === '/fastedge' || path.indexOf('/fastedge/') === 0;
  }

  function currentPath() {
    var fromAttr = document.documentElement.getAttribute('data-current-path');
    if (fromAttr) return fromAttr;
    return window.location.pathname;
  }

  function mount() {
    var path = currentPath();
    var existing = document.getElementById('fastedge-agent-setup');
    if (!isFastedge(path)) {
      if (existing && existing.parentNode) existing.parentNode.removeChild(existing);
      return true;
    }

    var place = tocPlace();
    if (!place) return false;
    if (isPlaced(existing, place)) return true;
    if (existing && existing.parentNode) existing.parentNode.removeChild(existing);

    var root = document.createElement('div');
    root.id = 'fastedge-agent-setup';

    var title = document.createElement('p');
    title.className = 'fastedge-agent-setup-title';
    title.textContent = 'Set up FastEdge with AI';
    root.appendChild(title);

    var agents = document.createElement('div');
    agents.className = 'fastedge-agent-setup-agents';
    root.appendChild(agents);

    var actions = document.createElement('div');
    actions.className = 'fastedge-agent-setup-actions';
    root.appendChild(actions);

    var copy = document.createElement('button');
    copy.type = 'button';
    copy.className = 'fastedge-agent-setup-copy';
    copy.textContent = 'Copy prompt';
    actions.appendChild(copy);

    var steps = document.createElement('a');
    steps.className = 'fastedge-agent-setup-steps';
    steps.href = '/fastedge/local-development/configure-plugin-and-mcp-server';
    steps.innerHTML = 'Setup guide<svg width="12" height="12" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>';
    actions.appendChild(steps);

    bindTip(copy, 'Copies one prompt for every agent. The agent downloads the FastEdge setup instructions and installs the plugin. An API token is not part of this prompt.');
    bindTip(steps, 'Opens the manual setup article: plugin install commands, an API token, the Docker fallback, and MCP clients without the plugin.');

    for (var k = 0; k < AGENTS.length; k++) {
      (function (agent) {
        var mark = document.createElement('span');
        mark.className = 'fastedge-agent-setup-agent';
        mark.setAttribute('data-agent', agent.id);
        mark.setAttribute('role', 'img');
        mark.setAttribute('aria-label', agent.label);
        mark.title = agent.label;
        mark.innerHTML = agent.svg;
        agents.appendChild(mark);
      })(AGENTS[k]);
    }

    copy.addEventListener('click', function () {
      function done() {
        copy.textContent = 'Copied';
        if (copiedTimer) window.clearTimeout(copiedTimer);
        copiedTimer = window.setTimeout(function () {
          copy.textContent = 'Copy prompt';
        }, 2000);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(PROMPT).then(done).catch(function () {});
        return;
      }
      done();
    });

    if (place.before) place.parent.insertBefore(root, place.before);
    else place.parent.appendChild(root);
    return true;
  }

  function isPlaced(existing, place) {
    if (!existing || existing.parentNode !== place.parent) return false;
    if (!place.before) return existing === place.parent.lastElementChild;
    return existing.nextElementSibling === place.before;
  }

  function tocPlace() {
    var toc = document.getElementById('table-of-contents');
    if (!toc) return null;
    // Preview renders the links inside nav. Local dev renders them directly in the TOC.
    var nav = toc.querySelector('nav');
    if (nav) return { parent: nav, before: null };
    return { parent: toc, before: null };
  }

  var pollId = null;
  var pollDeadline = 0;
  var applying = false;

  function ensure() {
    if (applying) return;
    applying = true;
    try {
      mount();
    } finally {
      applying = false;
    }
  }

  function startPolling() {
    watchContent();
    pollDeadline = Date.now() + 2000;
    if (pollId) return;
    pollId = window.setInterval(function () {
      ensure();
      if (Date.now() >= pollDeadline) {
        window.clearInterval(pollId);
        pollId = null;
      }
    }, 100);
  }

  function watchContent() {
    var root = document.body;
    if (!root || root.getAttribute('data-fastedge-agent-watch') === 'true') return;
    root.setAttribute('data-fastedge-agent-watch', 'true');
    var observer = new MutationObserver(function () {
      ensure();
    });
    observer.observe(root, { childList: true, subtree: true });
  }

  var origPushState = history.pushState.bind(history);
  history.pushState = function () {
    origPushState.apply(history, arguments);
    startPolling();
  };

  window.addEventListener('mintlify:navigate', startPolling);
  window.addEventListener('popstate', startPolling);

  function boot() {
    watchContent();
    startPolling();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
