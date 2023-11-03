#!/bin/bash

markdownlint './documentation'

if [ $? -ne 0 ]; then
  echo "The linting of Markdown files ended with errors."
  exit 1
fi
