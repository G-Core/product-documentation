function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // $& means the whole matched string
}

// This function finds and replaces text in the body of an HTML document.
// It traverses the DOM and only modifies text nodes, which is safer than using innerHTML.
function searchAndReplace(searchText, replacementText) {
  // Escape special characters in search text for use in regex.
  const safeSearchText = escapeRegExp(searchText);
  const walker = document.createTreeWalker(
    document.body,
    NodeFilter.SHOW_TEXT,
    null,
    false
  );

  let node;
  while ((node = walker.nextNode())) {
    // Using a regex with 'gi' flags for global and case-insensitive replacement
    const regex = new RegExp(safeSearchText, 'gi');
    node.nodeValue = node.nodeValue.replace(regex, replacementText);
  }
}

next.emmiter.on("routeChangeComplete", () => {
  searchAndReplace("___serverhost___", "example.com");
});