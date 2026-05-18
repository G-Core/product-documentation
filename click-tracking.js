(function () {
  'use strict';

  var COOKIE_DOMAIN = '.' + location.hostname.split('.').slice(-2).join('.');
  var COOKIE_TTL_MS = 30 * 60 * 1000;
  var COOKIE_OPTS = '; domain=' + COOKIE_DOMAIN + '; path=/; SameSite=Lax; Secure';

  function getCookie(name) {
    var m = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : null;
  }

  function setCookie(name, value) {
    var expires = '; expires=' + new Date(Date.now() + COOKIE_TTL_MS).toUTCString();
    document.cookie = name + '=' + encodeURIComponent(value) + COOKIE_OPTS + expires;
  }

  function setActionOnce(action, page) {
    if (getCookie('gc_action')) return;
    setCookie('gc_action', action);
    setCookie('gc_page', page);
  }

  var AUTH_LINK = [
    /auth\.gcore\.com/i,
    /api\.gcore\.com\/iam\/auth\/oauth2/i
  ];
  var SALES_LINK = [
    /gcore\.com\/contact-sales(?:[/?#]|$)/i
  ];

  function isTrackedLink(href) {
    return AUTH_LINK.concat(SALES_LINK).some(function (re) {
      return re.test(href);
    });
  }

  function getButtonText(el) {
    return (el.textContent || '').replace(/\s+/g, ' ').trim().substring(0, 100);
  }

  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[href]');
    if (!link || !isTrackedLink(link.href || '')) return;
    setActionOnce(getButtonText(link), location.pathname);
  }, true);
})();