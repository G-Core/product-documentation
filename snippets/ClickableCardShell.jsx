export const ClickableCardShell = ({ href, label, children }) => (
  <div className="homepage_clickable_card_wrap relative w-full">
    <a href={href} className="homepage_card_stretched_link" aria-label={label} />
    <div className="homepage_clickable_card_foreground relative z-10 w-full">
      {children}
    </div>
  </div>
);
