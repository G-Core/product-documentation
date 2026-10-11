# Rule for the Portal tab: MDX structure yes, style no

Applies whenever an API skill works in an article that has a `<MethodSection id="portal">`.

## Allowed — MDX structural rules (apply to Portal just like API)

- Adding missing `<p>` tags around bare prose paragraphs and numbered steps
- Fixing `1\.` → `1.` in numbered step format (MDX rendering rule, not style)
- Fixing `</MethodSection>` indentation (must be at column 0)
- Moving misplaced closing tags
- When content exists BEFORE `<MethodSwitch>`, move it inside the Portal section with ALL its headings, paragraphs, and structure intact — do not drop anything

## Forbidden — style, prose content, and structure (never touch in Portal)

- Rewriting "you/your" to neutral voice
- Fixing number style (1 → one)
- Fixing link text length
- Fixing `&nbsp;` in multi-word links
- Changing any prose wording
- Removing or renaming headings (`##`, `###`) that already exist
- Reordering sections or merging/splitting paragraphs
- Removing any sentence, phrase, or image that was already there

**Rule in one sentence:** Fix only the MDX syntax of Portal; never touch its content, headings, or prose — not even a single word.

**Critical failure to avoid:** When moving pre-MethodSwitch content into Portal, it is easy to move the first heading but forget subsequent headings. After the move, verify that ALL headings from the original shared content appear inside the Portal section.
