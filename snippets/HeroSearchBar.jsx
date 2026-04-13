"use client";

import {
  openMintlifyAskAI,
  openMintlifySearch,
} from "/snippets/mintlifyNavbarTriggers.js";

export function HeroSearchBar() {
  const shortcutLabel =
    typeof navigator !== "undefined" &&
    /Mac|iPhone|iPod|iPad/i.test(navigator.platform || "")
      ? "⌘K"
      : "Ctrl K";

  return (
    <div className="gcore_hero_search_wrap w-full max-w-2xl mt-2 relative z-10">
      <div
        className="gcore_hero_search_bar flex flex-row items-stretch rounded-xl border border-neutral-200 dark:border-neutral-700 bg-white dark:bg-neutral-950 shadow-sm overflow-hidden"
        role="group"
        aria-label="Search and Ask AI"
      >
        <button
          type="button"
          onClick={openMintlifySearch}
          className="gcore_hero_search_left flex flex-1 min-w-0 items-center gap-3 px-4 py-3 text-left hover:bg-neutral-50 dark:hover:bg-neutral-900 transition-colors"
        >
          <svg
            className="w-5 h-5 shrink-0 text-neutral-400"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            aria-hidden={true}
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
            />
          </svg>
          <span className="text-neutral-400 text-sm flex-1 truncate">
            Search documentation...
          </span>
          <kbd className="hidden sm:inline-flex items-center rounded border border-neutral-200 dark:border-neutral-600 px-1.5 py-0.5 text-xs text-neutral-500 font-sans bg-neutral-50 dark:bg-neutral-900">
            {shortcutLabel}
          </kbd>
        </button>
        <div
          className="w-px bg-neutral-200 dark:bg-neutral-700 self-stretch shrink-0"
          aria-hidden={true}
        />
        <button
          type="button"
          onClick={openMintlifyAskAI}
          className="gcore_hero_search_ai flex items-center gap-2 px-4 py-3 text-orange-600 dark:text-orange-500 font-medium text-sm shrink-0 hover:bg-orange-50 dark:hover:bg-orange-950/30 transition-colors"
        >
          <svg
            className="w-5 h-5 shrink-0"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="currentColor"
            aria-hidden={true}
          >
            <path d="M9.813 15.904 9 18.75l-.813-2.846a4.5 4.5 0 0 0-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 0 0 3.09-3.09L9 5.25l.813 2.847a4.5 4.5 0 0 0 3.09 3.09L15.75 12l-2.847.813a4.5 4.5 0 0 0-3.09 3.09ZM18.259 8.715 18 9.75l-.259-1.035a3.375 3.375 0 0 0-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 0 0 2.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 0 0 2.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 0 0-2.456 2.456ZM16.894 20.567 16.5 21.75l-.394-1.183a2.25 2.25 0 0 0-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 0 0 1.423-1.423L16.5 15.75l.394 1.183a2.25 2.25 0 0 0 1.423 1.423L19.5 18.75l-1.183.394a2.25 2.25 0 0 0-1.423 1.423Z" />
          </svg>
          Ask AI
        </button>
      </div>
    </div>
  );
}
