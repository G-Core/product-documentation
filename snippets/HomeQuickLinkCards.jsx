"use client";

import { openMintlifyAskAI } from "/snippets/mintlifyNavbarTriggers.js";

function IconChart() {
  return (
    <svg
      className="h-6 w-6 text-orange-600 dark:text-orange-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      strokeWidth={1.5}
      stroke="currentColor"
      aria-hidden
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 0 1 3 19.875v-6.75ZM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V8.625ZM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V4.125Z"
      />
    </svg>
  );
}

function IconTerminal() {
  return (
    <svg
      className="h-6 w-6 text-orange-600 dark:text-orange-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      strokeWidth={1.5}
      stroke="currentColor"
      aria-hidden
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        d="M6.75 7.5h.008v.008H6.75V7.5Zm6.75 0h.008v.008h-.008V7.5Zm-6.75 3.75h.008v.008H6.75v-.008Zm3.75 0h.008v.008H10.5v-.008Zm-5.25-6h12a1.5 1.5 0 0 1 1.5 1.5v12a1.5 1.5 0 0 1-1.5 1.5h-12a1.5 1.5 0 0 1-1.5-1.5v-12a1.5 1.5 0 0 1 1.5-1.5Zm3 6 2.25 2.25L9 15.75m3.75-3h3"
      />
    </svg>
  );
}

function IconSparkles() {
  return (
    <svg
      className="h-6 w-6 text-orange-600 dark:text-orange-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
      aria-hidden
    >
      <path d="M9.813 15.904 9 18.75l-.813-2.846a4.5 4.5 0 0 0-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 0 0 3.09-3.09L9 5.25l.813 2.847a4.5 4.5 0 0 0 3.09 3.09L15.75 12l-2.847.813a4.5 4.5 0 0 0-3.09 3.09ZM18.259 8.715 18 9.75l-.259-1.035a3.375 3.375 0 0 0-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 0 0 2.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 0 0 2.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 0 0-2.456 2.456ZM16.894 20.567 16.5 21.75l-.394-1.183a2.25 2.25 0 0 0-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 0 0 1.423-1.423L16.5 15.75l.394 1.183a2.25 2.25 0 0 0 1.423 1.423L19.5 18.75l-1.183.394a2.25 2.25 0 0 0-1.423 1.423Z" />
    </svg>
  );
}

function QuickCard({ href, title, description, icon, isAction, onAction }) {
  const inner = (
    <>
      <div className="homepage_quick_link_icon_wrap flex h-11 w-11 shrink-0 items-center justify-center rounded-lg bg-orange-50 dark:bg-orange-950/40">
        {icon}
      </div>
      <div className="min-w-0 flex-1 text-left">
        <div className="font-semibold text-neutral-900 dark:text-neutral-100">
          {title}
        </div>
        <div className="mt-0.5 text-sm text-neutral-600 dark:text-neutral-400">
          {description}
        </div>
      </div>
    </>
  );

  const className =
    "homepage_quick_link_card group flex w-full items-center gap-4 rounded-xl border border-neutral-200 bg-white p-4 transition-colors hover:border-orange-500 dark:border-neutral-700 dark:bg-neutral-950 dark:hover:border-orange-600";

  if (isAction) {
    return (
      <button
        type="button"
        className={className}
        onClick={onAction}
        aria-label={`${title}: ${description}`}
      >
        {inner}
      </button>
    );
  }

  return (
    <a href={href} className={className} aria-label={`${title}: ${description}`}>
      {inner}
    </a>
  );
}

export function HomeQuickLinkCards() {
  return (
    <div className="homepage_quick_links mt-8 grid w-full max-w-5xl grid-cols-1 gap-4 sm:grid-cols-3">
      <QuickCard
        href="/cloud"
        title="Get started"
        description="New to Gcore? Start here"
        icon={<IconChart />}
      />
      <QuickCard
        href="/api-reference/overview"
        title="API reference"
        description="Manage resources via API"
        icon={<IconTerminal />}
      />
      <QuickCard
        title="What are you building?"
        description="Find the right product with AI assistant"
        icon={<IconSparkles />}
        isAction
        onAction={openMintlifyAskAI}
      />
    </div>
  );
}
