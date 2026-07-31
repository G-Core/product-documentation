export const MethodTabs = ({ methods }) => {
  const [currentPath, setCurrentPath] = React.useState("");

  React.useEffect(() => {
    const getSidebar = () => document.querySelector("#sidebar-content");

    setCurrentPath(window.location.pathname);

    const saved = sessionStorage.getItem("methodTabsSidebarScroll");
    console.log("[MethodTabs] mount, saved=", saved, "scrollTop=", getSidebar()?.scrollTop);
    if (saved === null) return;
    sessionStorage.removeItem("methodTabsSidebarScroll");

    const target = parseInt(saved, 10);
    if (target === 0) return;

    let mounted = true;
    const until = Date.now() + 1500;
    let frames = 0;

    const restore = () => {
      if (!mounted) return;
      const container = getSidebar();
      if (container) {
        if (container.scrollTop !== target) {
          console.log("[MethodTabs] frame", frames, "scrollTop=", container.scrollTop, "-> setting", target);
          container.scrollTop = target;
        }
      }
      frames++;
      if (Date.now() < until) {
        requestAnimationFrame(restore);
      } else {
        console.log("[MethodTabs] done, final scrollTop=", getSidebar()?.scrollTop);
      }
    };

    requestAnimationFrame(restore);
    return () => { mounted = false; };
  }, []);

  const handleClick = () => {
    const container = document.querySelector("#sidebar-content");
    const st = container?.scrollTop ?? null;
    console.log("[MethodTabs] click, saving scrollTop=", st);
    if (container) {
      sessionStorage.setItem("methodTabsSidebarScroll", String(container.scrollTop));
    }
  };

  return (
    <div
      className="not-prose flex gap-0 border-b border-zinc-200 dark:border-zinc-800 mb-8 mt-2"
      role="tablist"
    >
      {methods.map(({ label, href, soon }) => {
        const isActive = currentPath.length > 0 && currentPath.endsWith(href);
        const Tag = soon || !href ? "span" : "a";
        return (
          <Tag
            key={href || label}
            href={soon || !href ? undefined : href}
            role="tab"
            aria-selected={isActive}
            onClick={!soon && href ? handleClick : undefined}
            className={[
              "px-4 py-2 text-sm font-medium border-b-2 -mb-px transition-colors select-none",
              isActive
                ? "border-primary text-primary"
                : soon
                ? "border-transparent text-zinc-400 cursor-default"
                : "border-transparent text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 cursor-pointer",
            ].join(" ")}
          >
            {label}
            {soon ? " (soon)" : ""}
          </Tag>
        );
      })}
    </div>
  );
};
