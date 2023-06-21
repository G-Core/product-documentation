#!/usr/bin/env sh

patch_envs() {
  local file=$1
  local tmp=$( ( echo "cat <<EOF" ; cat "$file" ) | sh)
  echo "$tmp" > $file
}

patch_envs dist/product-documentation/docs/config.js