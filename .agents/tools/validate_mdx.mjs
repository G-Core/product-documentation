// Compile one MDX file and print OK or the exact error. Run through validate_mdx.ps1.
import { compile } from '@mdx-js/mdx';
import { readFileSync } from 'node:fs';

const file = process.argv[2];
if (!file) {
  console.error('Usage: node validate_mdx.mjs <absolute path to article.mdx>');
  process.exit(2);
}

try {
  await compile(readFileSync(file, 'utf8'));
  console.log('OK');
} catch (e) {
  console.error('ERROR:', e.message);
  process.exit(1);
}
