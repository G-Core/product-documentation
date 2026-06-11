# Procedures — Writing Step-by-Step Instructions

Rules for writing numbered steps in how-to articles and tutorials.
Load this file when a skill tells you to write or review procedural content.

---

## Step format

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
2. Go to Cloud > Virtual Machines.
```

**Correct:**
```
1. Log in to the [Gcore Customer Portal](https://portal.gcore.com) and go to
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
