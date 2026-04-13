/**
 * Footer line "Gcore {year}" using the calendar year in Europe/Luxembourg (IANA TZ).
 * Loaded globally by Mintlify with other .js files in the documentation root.
 */
(function () {
  var TZ = "Europe/Luxembourg";

  function yearInLuxembourg() {
    return new Intl.DateTimeFormat("en-GB", {
      timeZone: TZ,
      year: "numeric",
    }).format(new Date());
  }

  function ensureFooterCopyright() {
    var footer =
      document.getElementById("footer") ||
      document.querySelector('[data-component-name="footer"]') ||
      document.querySelector("footer");
    if (!footer) {
      return false;
    }

    var slot = document.getElementById("gcore-footer-copyright");
    var yearEl = document.querySelector(".gcore-footer-copyright-year");

    if (slot && yearEl) {
      yearEl.textContent = yearInLuxembourg();
      return true;
    }

    slot = document.createElement("div");
    slot.id = "gcore-footer-copyright";
    slot.className = "gcore-footer-copyright";
    slot.setAttribute("aria-label", "Copyright");

    yearEl = document.createElement("span");
    yearEl.className = "gcore-footer-copyright-year";
    yearEl.textContent = yearInLuxembourg();

    slot.appendChild(document.createTextNode("Gcore "));
    slot.appendChild(yearEl);

    footer.appendChild(slot);
    return true;
  }

  function run() {
    ensureFooterCopyright();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
  window.addEventListener("load", run);

  var tries = 0;
  var poll = setInterval(function () {
    tries += 1;
    if (ensureFooterCopyright() || tries >= 48) {
      clearInterval(poll);
    }
  }, 200);
})();
