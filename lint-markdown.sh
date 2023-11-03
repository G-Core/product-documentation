#!/bin/bash

# Выполнить линтинг Markdown-файлов в указанной директории
markdownlint './documentation'

# Проверить код возврата линтера
if [ $? -ne 0 ]; then
  echo "The linting of Markdown files ended with errors."
  exit 1  # Завершить сборку с ошибкой
fi
