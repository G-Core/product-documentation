# Procedures — Writing Step-by-Step Instructions

Rules for writing numbered steps in how-to articles and tutorials.
Load this file when a skill tells you to write or review procedural content.

---

## Choosing the format: numbered list or `<Steps>`

Decide by the size of the steps in the whole procedure.

- **All steps short: plain numbered list.** Each step is a single action that fits in a sentence or two, for example "Click **Save**." or a step with a short list of values to enter. Follow the rules in this file.
- **Steps are large, or the sizes are mixed: `<Steps>` with `<Step title="...">`.** One format for the whole procedure. If at least one step is large and the others are short, the whole procedure uses `<Steps>`. Follow `mdx-rules.md`, "Steps component", and `style-guide.md`, "Use `<Steps>` for procedures with large steps".

Never nest `<Steps>` inside `<Steps>`. Inside a `<Step>` body, write sub-actions as a flat numbered list.

### Three forms of a `<Step>`

Pick the form by the size of the step. The title and the body must never duplicate each other.

1. **Very small step: the action is the title, no body.** A very small step does not need a separate paragraph.
   ```mdx
   <Step title="Click **Save**"></Step>
   ```
2. **Step with a little explanation: the action or goal is the title, the explanation is the body.** The body adds what the title does not say.
   ```mdx
   <Step title="Select a region">
     Choose the region closest to the users. The region cannot be changed after creation.
   </Step>
   ```
3. **Large, complex step: the goal is the title, the content is in the body.** The body holds the full content: a numbered sub-list, screenshots, callouts.
   ```mdx
   <Step title="Add a CNAME record">
     Click **Add record** and fill in the form:

     1. Set **Type** to **CNAME**.
     2. In the **Name** field, enter the root domain.
     3. Click **Add**.

     <Frame>![Add CNAME record form](/images/docs/...)</Frame>
   </Step>
   ```

---

## Step format (numbered list)

```mdx
1. Navigate to **Settings** > **API Keys**.

2. Click **Create New Key**.

3. In the dialog:
   - Enter a **Name** for the key
   - Select the **Permissions**
   - Click **Create**

4. Copy the key and store it securely.
```

Blank line between every numbered item. Sub-items indent 3 spaces under their parent.

Inside `<MethodSection>` (tabbed articles) write each numbered step as `<p>1. text</p>` instead; plain `1.` items merge into one paragraph there. See `mdx-rules.md`, "Content rules inside `<MethodSection>`".

---

## Order within a step

### Location before action

State where the reader must go before telling them what to do.

| Bad | Good |
|-----|------|
| "Select **Add record** in the **DNS** section." | "In the **DNS** section, select **Add record**." |
| "Click **Save** on the settings page." | "On the settings page, click **Save**." |

### Purpose before action

State why the reader is doing something before the action itself — when the purpose
is not already obvious from context.

| Bad | Good |
|-----|------|
| "Select **Delete** to remove the rule." | "To remove the rule, select **Delete**." |
| "Click **Verify** to confirm the certificate." | "To confirm the certificate, click **Verify**." |

Do not apply this rule mechanically to every step — only when the purpose adds
meaningful context. "To save, click **Save**" is tautological and should be
just "Click **Save**."

---

## Navigation paths

Write navigation paths with `>` as the separator and bold for each UI element: `navigate to **Section** > **Subsection**`. Do not use arrows.

---

## Optional steps

Prefix optional steps with exactly `(Optional)` as the first word:

```
(Optional) Enter a description for the key.
```

Not "Optional:", not "(optional)", not "Optionally, ...". The exact prefix is `(Optional)`.

---

## Login steps

Write "log in to" as three words. Never "log into".

**Wrong:** "Log into the Gcore Customer Portal."
**Correct:** "Log in to the [Gcore Customer Portal](https://portal.gcore.com)."

Consolidate login and navigation into a single step when they are always done together:

**Over-split:**
```
1. Log in to the Customer Portal.
2. Navigate to Cloud > Virtual Machines.
```

**Correct:**
```
1. Log in to the [Gcore Customer Portal](https://portal.gcore.com) and navigate to
   **Cloud** > **Virtual Machines**.
```

---

## Single-step procedures

Do not create a numbered list for a single step. Fold the action into the
introductory sentence instead.

**Wrong:**
```
To reset your password:

1. Click **Forgot password** on the login page.
```

**Correct:**
```
To reset your password, click **Forgot password** on the login page.
```

---

## Sub-step hierarchy

For nested steps, use letters then Roman numerals:

```
1. Configure the listener:
   a. Set **Protocol** to HTTPS.
   b. Set **Port** to 443.
   c. Add a certificate:
      i. Click **Add certificate**.
      ii. Select the certificate from the list.
```

Do not go deeper than three levels (number → letter → Roman numeral). If a procedure
requires a fourth level, restructure it into separate top-level steps.

The letter and Roman numeral levels apply to plain numbered lists. Inside a `<Step>` body use a flat numbered list, because `<Steps>` already provides the top level.

---

## Numbered vs. bullet lists

Use numbered lists only when order matters and skipping a step would break the flow.
If steps can be done in any order, use bullet points.

| Use numbers | Use bullets |
|-------------|-------------|
| Configuring a resource in sequence | Listing supported formats |
| Installation steps | Feature capabilities |
| Troubleshooting steps that build on each other | Prerequisites already met |

---

## Notes and warnings in procedures

Use MDX components for callouts within steps. Place them after the step text
they relate to — not before.

```mdx
<Note>
Supplementary context that is not critical to completing the step.
</Note>

<Warning>
Information the reader must know to avoid data loss or breakage.
</Warning>

<Tip>
Best practice or shortcut the reader might find useful.
</Tip>

<Info>
Prerequisites, access requirements, or environment setup.
</Info>
```

Callout rules:
- One callout per step maximum
- No "you" or "your" inside callouts — same rule as prose
- Keep callouts to 1–2 sentences. If more is needed, it belongs in the step text.

---

## What not to do

- Do not start step text with a gerund: "Selecting **Save**" → "Select **Save**"
- Do not number steps that are not sequential — use bullets
- Do not add "Please" in instructions
- Do not use directional language: not "click the button on the right" — reference by name
- Do not document keyboard shortcuts in procedures
