export const ChangelogDashboard = ({ data }) => {
  const PREVIEW_COUNT = 5;
  const OPEN_AT_START = 3;
  const ICONS = {
    cloud: "/images/docs/portal-icons/cloud.svg",
    cdn: "/images/docs/portal-icons/cdn.svg",
    "ddos-protection": "/images/docs/portal-icons/ddos.svg",
    "edge-proxy": "/images/docs/portal-icons/shield_proxy.svg",
    "edge-ai": "/images/docs/portal-icons/ai_infrastructure.svg",
    streaming: "/images/docs/portal-icons/streaming.svg",
    waap: "/images/docs/portal-icons/waap.svg",
    "account-settings": "/images/docs/portal-icons/user.svg",
    dns: "/images/docs/portal-icons/dns.svg",
    fastedge: "/images/docs/portal-icons/fast_edge.svg",
    gclaw: "/images/docs/portal-icons/gclaw.svg",
    hosting: "/images/docs/portal-icons/basic_vm.svg",
    storage: "/images/docs/portal-icons/storage.svg",
  };

  const Icon = ({ name }) => {
    const src = ICONS[name];
    if (src) {
      return React.createElement("img", { className: "changelog-icon", src: src, alt: "" });
    }
    return React.createElement(
      "svg",
      { className: "changelog-icon", viewBox: "0 0 24 24", "aria-hidden": "true" },
      React.createElement("path", { d: "M12 3l1.2 3.2L16.5 7.5 13.2 8.7 12 12l-1.2-3.3L7.5 7.5l3.3-1.3L12 3z" })
    );
  };

  const RichText = ({ text }) => {
    const parts = String(text || "").split("`");
    return parts.map((part, index) =>
      index % 2 === 1
        ? React.createElement("code", { key: index }, part)
        : React.createElement("span", { key: index }, part)
    );
  };

  const matches = (item, query, kind) => {
    if (kind !== "all" && item.kind !== kind) return false;
    if (!query) return true;
    const haystack = `${item.title} ${item.summary} ${item.guideLabel}`.toLowerCase();
    return haystack.includes(query);
  };

  const products = (data && data.products) || [];
  const items = (data && data.items) || [];
  const [productId, setProductId] = React.useState("all");
  const [kind, setKind] = React.useState("all");
  const [query, setQuery] = React.useState("");
  const [openProducts, setOpenProducts] = React.useState(() => new Set(products.slice(0, OPEN_AT_START).map((product) => product.id)));
  const [expanded, setExpanded] = React.useState(() => new Set());
  const [archive, setArchive] = React.useState(() => new Set());

  const needle = query.trim().toLowerCase();
  const searching = needle !== "" || kind !== "all";
  const filtering = searching || productId !== "all";

  React.useEffect(() => {
    const hash = window.location.hash.replace(/^#/, "");
    if (!hash) return;
    const item = items.find((entry) => entry.id === hash);
    const folder = item ? item.product : products.some((product) => product.id === hash) ? hash : "";
    if (!folder) return;
    setOpenProducts((current) => new Set(current).add(folder));
    if (item) {
      const index = items.filter((entry) => entry.product === folder).findIndex((entry) => entry.id === item.id);
      if (index >= PREVIEW_COUNT) {
        setArchive((current) => new Set(current).add(folder));
      }
    }
    window.setTimeout(() => {
      const target = document.getElementById(hash);
      if (target) target.scrollIntoView({ block: "start" });
    }, 0);
  }, []);

  const visibleItems = items.filter((item) => {
    if (productId !== "all" && item.product !== productId) return false;
    return matches(item, needle, kind);
  });

  const byProduct = {};
  visibleItems.forEach((item) => {
    if (!byProduct[item.product]) byProduct[item.product] = [];
    byProduct[item.product].push(item);
  });

  const showArchive = (id) => {
    setOpenProducts((current) => new Set(current).add(id));
    setArchive((current) => new Set(current).add(id));
    window.setTimeout(() => {
      const target = document.getElementById(id);
      if (target) target.scrollIntoView({ block: "start" });
    }, 0);
  };

  const renderEntry = (item) => (
    <article key={item.id} className="changelog-entry" id={item.id}>
      <span className="changelog-dot changelog-dot-entry" />
      <span className={`changelog-kind changelog-kind-${item.kind}`}>{item.kindLabel}</span>
      <div className="changelog-entry-meta">
        {item.shortMonth}
        <span>{" · "}</span>
        {item.guideLabel}
      </div>
      <a className="changelog-entry-link" href={item.guideUrl}>
        {React.createElement(RichText, { text: item.summary })}
      </a>
    </article>
  );

  const toggleProduct = (id) => {
    setOpenProducts((current) => {
      const next = new Set(current);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const shownProducts = products.filter((product) => productId === "all" || product.id === productId);

  return (
    <div className="changelog-dashboard">
      <div className="changelog-top">
        <div>
          <h1 className="changelog-heading">Gcore changelog</h1>
        </div>
        <div className="changelog-toolbar">
          <input
            className="changelog-search"
            type="search"
            value={query}
            placeholder="Search updates..."
            aria-label="Search updates"
            onChange={(event) => setQuery(event.target.value)}
          />
          <select className="changelog-select" aria-label="Product" value={productId} onChange={(event) => setProductId(event.target.value)}>
            <option value="all">All products</option>
            {products.map((product) => (
              <option key={product.id} value={product.id}>{product.label}</option>
            ))}
          </select>
          <select className="changelog-select" aria-label="Type" value={kind} onChange={(event) => setKind(event.target.value)}>
            <option value="all">All types</option>
            <option value="new">New</option>
            <option value="improved">Improved</option>
            <option value="fixed">Fixed</option>
          </select>
        </div>
      </div>

      <div className="changelog-layout">
        <nav className="changelog-nav" aria-label="Products">
          <button type="button" className={productId === "all" ? "changelog-nav-item is-active" : "changelog-nav-item"} onClick={() => setProductId("all")}>
            {React.createElement(Icon, { name: "all" })}
            <span>All products</span>
            <span className="changelog-count">{items.length}</span>
          </button>
          {products.map((product) => (
            <button
              key={product.id}
              type="button"
              className={productId === product.id ? "changelog-nav-item is-active" : "changelog-nav-item"}
              onClick={() => setProductId(product.id)}
            >
              {React.createElement(Icon, { name: product.id })}
              <span>{product.label}</span>
              <span className="changelog-count">{product.count}</span>
            </button>
          ))}
        </nav>

        <div className="changelog-main">
          {shownProducts.length === 0 || visibleItems.length === 0 ? (
            <p className="changelog-empty">No updates match.</p>
          ) : null}
          {shownProducts.map((product) => {
            const own = byProduct[product.id] || [];
            if (own.length === 0) return null;
            const open = filtering || openProducts.has(product.id);
            const showAll = searching || expanded.has(product.id) || archive.has(product.id);
            const listed = showAll ? own : own.slice(0, PREVIEW_COUNT);
            const hidden = own.length - listed.length;
            const months = [];
            if (archive.has(product.id)) {
              listed.forEach((item) => {
                const last = months[months.length - 1];
                if (!last || last.label !== item.month) months.push({ label: item.month, items: [item] });
                else last.items.push(item);
              });
            }
            return (
              <section key={product.id} className="changelog-card" id={product.id}>
                <header className="changelog-card-head">
                  <button type="button" className="changelog-card-title" onClick={() => toggleProduct(product.id)}>
                    {React.createElement(Icon, { name: product.id })}
                    <span>{product.label}</span>
                    <span className="changelog-pill">{own.length} updates</span>
                  </button>
                  <button type="button" className="changelog-view-all" onClick={() => showArchive(product.id)}>
                    {`View all ${product.label} updates`}
                    <span aria-hidden="true">{"\u2192"}</span>
                  </button>
                </header>
                {open ? (
                  <div className="changelog-card-body">
                    {archive.has(product.id) ? months.map((month) => (
                      <div key={month.label} className="changelog-month">
                        <div className="changelog-month-label">
                          <span className="changelog-dot" />
                          {month.label}
                        </div>
                        {month.items.map(renderEntry)}
                      </div>
                    )) : (
                      <div className="changelog-month">
                        {listed.map(renderEntry)}
                        {hidden > 0 ? (
                          <button type="button" className="changelog-more" onClick={() => setExpanded((current) => new Set(current).add(product.id))}>
                            + {hidden} more updates
                          </button>
                        ) : null}
                      </div>
                    )}
                  </div>
                ) : null}
              </section>
            );
          })}
        </div>
      </div>
    </div>
  );
};
