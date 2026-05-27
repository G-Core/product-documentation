export const MethodTabs = ({ methods }) => {
  const [currentPath, setCurrentPath] = React.useState("");

  React.useEffect(() => {
    setCurrentPath(window.location.pathname);
  }, []);

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
