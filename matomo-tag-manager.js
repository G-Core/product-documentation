(function () {
  'use strict';

  var mtm = (window._mtm = window._mtm || []);
  mtm.push({ 'mtm.startTime': new Date().getTime(), event: 'mtm.Start' });

  var container = document.createElement('script');
  container.async = true;
  container.src = 'https://gcore.com/analytics/matomo/js/container_e8h8zW9U.js';

  var firstScript = document.getElementsByTagName('script')[0];
  firstScript.parentNode.insertBefore(container, firstScript);
})();
