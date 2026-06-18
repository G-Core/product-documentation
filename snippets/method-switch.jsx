export const MethodSection = ({ children }) => children ?? null;

export const MethodSwitch = ({ children }) => {
  const tabs = React.Children.toArray(children).filter(
    (c) => c && c.props && c.props.id
  );
  const firstId = tabs.length > 0 ? tabs[0].props.id : "";

  const [active, setActive] = React.useState(firstId);

  React.useEffect(() => {
    try {
      const saved = localStorage.getItem("gcore_docs_method");
      if (saved && tabs.find((t) => t.props.id === saved)) {
        setActive(saved);
      }
    } catch (_) {}
  }, []);

  React.useEffect(() => {
    try {
      document.querySelectorAll("h2[id], h3[id]").forEach((heading) => {
        const visible = heading.offsetParent !== null;
        document
          .querySelectorAll(`a[href="#${heading.id}"]`)
          .forEach((link) => {
            if (link.closest("h1,h2,h3,h4,h5,h6")) return;
            const li = link.closest("li");
            if (li) li.style.display = visible ? "" : "none";
          });
      });
    } catch (_) {}
  }, [active]);

  const handleClick = (id) => {
    setActive(id);
    try {
      localStorage.setItem("gcore_docs_method", id);
    } catch (_) {}
  };

  return (
    <div>
      <div
        className="not-prose flex gap-0 border-b border-zinc-200 dark:border-zinc-800 mb-8 mt-2"
        role="tablist"
      >
        {tabs.map((tab) => {
          const isActive = active === tab.props.id;
          return (
            <button
              key={tab.props.id}
              role="tab"
              aria-selected={isActive}
              onClick={() => handleClick(tab.props.id)}
              className={[
                "px-4 py-2 text-sm font-medium border-b-2 -mb-px transition-colors cursor-pointer",
                isActive
                  ? "border-primary text-primary"
                  : "border-transparent text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200",
              ].join(" ")}
            >
              {tab.props.label}
            </button>
          );
        })}
      </div>

      {tabs.map((tab) => (
        <div
          key={tab.props.id}
          style={{ display: active === tab.props.id ? "" : "none" }}
        >
          {tab.props.children}
        </div>
      ))}
    </div>
  );
};
