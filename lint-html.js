const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const rootFolder = './documentation';

const dangerousElements = ['script', 'object'];
const dangerousAttributes = ['onclick', 'onload'];

function isInsideCodeBlock(element) {
  let currentElement = element;
  while (currentElement) {
    if (currentElement.name === 'code') { // Исключаем блоки <code>
      return true;
    }
    currentElement = currentElement.parent;
  }
  return false;
}

function checkForDangerousTags(file) {
  const content = fs.readFileSync(file, 'utf8');
  const $ = cheerio.load(content, { xmlMode: true });

  let foundDangerous = false;

  $('*').each((index, element) => {
    if (dangerousElements.includes(element.name) && !isInsideCodeBlock(element)) {
      console.error(`В файле ${file} найден потенциально опасный тег: ${element.name}`);
      foundDangerous = true;
    }

    for (const attribute of dangerousAttributes) {
      if (element.attribs[attribute] && !isInsideCodeBlock(element)) {
        console.error(`В файле ${file} найден потенциально опасный атрибут: ${attribute}`);
        foundDangerous = true;
      }
    }
  });

  if (foundDangerous) {
    process.exit(1);
  }
}

function processFilesInDirectory(directory) {
  const files = fs.readdirSync(directory);

  for (const file of files) {
    const filePath = path.join(directory, file);

    if (fs.statSync(filePath).isDirectory()) {
      processFilesInDirectory(filePath);
    } else if (file.endsWith('.md')) {
      checkForDangerousTags(filePath);
    }
  }
}

processFilesInDirectory(rootFolder);

console.log('Проверка успешно завершена.');
