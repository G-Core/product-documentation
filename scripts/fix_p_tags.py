#!/usr/bin/env python3
"""
Wrap bare prose paragraphs in <p> tags inside <MethodSection> blocks.
Only wraps direct children of MethodSection (not inside Info, Warning, Tabs, etc.).
"""
import re
from pathlib import Path

BLOCK_COMPONENTS = {
    'Info', 'Warning', 'Tip', 'Note', 'Tabs', 'Tab',
    'Accordion', 'AccordionGroup', 'Frame', 'CodeGroup',
    'Check', 'Card', 'CardGroup', 'Steps', 'Step',
    'Callout', 'Expandable', 'Tooltip',
}

OPEN_RE = {c: re.compile(rf'<{c}(\s[^>]*)?>') for c in BLOCK_COMPONENTS}
CLOSE_RE = {c: re.compile(rf'</{c}>') for c in BLOCK_COMPONENTS}
SELFCLOSE_RE = {c: re.compile(rf'<{c}(\s[^>]*)?/>') for c in BLOCK_COMPONENTS}


def is_prose_line(stripped: str) -> bool:
    if not stripped:
        return False
    if stripped.startswith('#'):
        return False
    if stripped.startswith('```'):
        return False
    if stripped.startswith('<'):
        return False
    # standard markdown list items
    if stripped.startswith('- ') or stripped.startswith('* ') or stripped.startswith('+ '):
        return False
    # real markdown numbered list: "1. text" (period+space, no backslash)
    # "1\. text" (MDX-escaped) is NOT a list item — it is prose and needs <p>
    if re.match(r'^\d+\. ', stripped):
        return False
    if stripped.startswith('|'):
        return False
    if stripped.startswith('>'):
        return False
    if stripped.startswith('!'):
        return False
    return True


def process_content(content: str) -> str:
    lines = content.split('\n')
    result = []
    in_method_section = False
    inner_depth = 0
    in_code_fence = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # track code fences
        if stripped.startswith('```'):
            in_code_fence = not in_code_fence
            result.append(line)
            i += 1
            continue

        if in_code_fence:
            result.append(line)
            i += 1
            continue

        # MethodSection entry
        if re.search(r'<MethodSection\b', line):
            in_method_section = True
            inner_depth = 0
            result.append(line)
            i += 1
            continue

        # MethodSection exit
        if '</MethodSection>' in line:
            in_method_section = False
            inner_depth = 0
            result.append(line)
            i += 1
            continue

        if not in_method_section:
            result.append(line)
            i += 1
            continue

        # track component depth (update BEFORE checking prose)
        for comp in BLOCK_COMPONENTS:
            opens_selfclose = len(SELFCLOSE_RE[comp].findall(line))
            opens_all = len(OPEN_RE[comp].findall(line))
            opens = opens_all - opens_selfclose
            closes = len(CLOSE_RE[comp].findall(line))
            # self-closing tags: open_all includes self-closing in some cases, subtract them
            # better: count non-self-closing opens as opens_all - opens_selfclose
            inner_depth += opens - closes

        # clamp to 0 in case of unbalanced tags
        if inner_depth < 0:
            inner_depth = 0

        # wrap prose at depth 0
        if inner_depth == 0 and is_prose_line(stripped):
            # collect consecutive prose lines forming one paragraph
            para = [stripped]
            j = i + 1
            while j < len(lines):
                ns = lines[j].strip()
                if not ns:
                    break
                if not is_prose_line(ns):
                    break
                # stop if next line would change component depth
                changes = False
                for comp in BLOCK_COMPONENTS:
                    if OPEN_RE[comp].search(lines[j]) or CLOSE_RE[comp].search(lines[j]):
                        changes = True
                        break
                if changes:
                    break
                para.append(ns)
                j += 1

            if len(para) == 1:
                result.append(f'<p>{para[0]}</p>')
            else:
                result.append(f'<p>{para[0]}')
                for pl in para[1:-1]:
                    result.append(pl)
                result.append(f'{para[-1]}</p>')
            i += len(para)
        else:
            result.append(line)
            i += 1

    return '\n'.join(result)


def process_file(filepath: str) -> int:
    path = Path(filepath)
    original = path.read_text(encoding='utf-8')
    updated = process_content(original)
    if updated != original:
        path.write_text(updated, encoding='utf-8')
        # count wrapped paragraphs
        added = updated.count('<p>') - original.count('<p>')
        return added
    return 0


FILES = [
    'cloud/networking/create-and-manage-a-network.mdx',
    'cloud/networking/create-and-manage-a-subnetwork.mdx',
    'cloud/networking/create-and-manage-a-router.mdx',
    'cloud/networking/add-and-configure-a-firewall.mdx',
    'cloud/virtual-instances/volumes/create-and-configure-volumes.mdx',
    'cloud/virtual-instances/placement-groups/configure-a-placement-group.mdx',
    'cloud/virtual-instances/create-an-instance.mdx',
    'cloud/virtual-instances/customize-initial-setup-for-your-instance.mdx',
    'cloud/virtual-instances/check-the-operational-status-of-your-instance.mdx',
    'cloud/networking/ip-address/create-and-configure-a-floating-ip-address.mdx',
    'cloud/networking/ip-address/create-and-configure-a-reserved-ip-address.mdx',
    'cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address.mdx',
    'cloud/secrets-manager/upload-a-pkcs12-file.mdx',
]

if __name__ == '__main__':
    total = 0
    for f in FILES:
        n = process_file(f)
        print(f'{f}: +{n} <p> wraps')
        total += n
    print(f'\nTotal: {total} paragraphs wrapped')
