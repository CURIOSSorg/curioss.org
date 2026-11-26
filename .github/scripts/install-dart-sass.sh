#!/usr/bin/env bash
# Install Dart Sass for Linux x64, which Hugo needs to compile the site's SCSS.
# Used by GitHub Actions (.github/actions/setup-hugo) and Netlify (netlify.toml).
#
#   install-dart-sass.sh <directory>   then add <directory> to PATH
#
# To upgrade, change both the version and the checksum. The checksum is on the
# release page: https://github.com/sass/dart-sass/releases
set -euo pipefail

version="1.108.2"
sha256="32d2eb5b83cbc180fce9657ff3c57401a9006c59eccfe0bfdde0aa755a66d42f"
directory="$1"

archive="$(mktemp)"
curl -fsSL -o "$archive" "https://github.com/sass/dart-sass/releases/download/${version}/dart-sass-${version}-linux-x64.tar.gz"
echo "${sha256}  ${archive}" | sha256sum --check --quiet
mkdir -p "$directory"
tar -xzf "$archive" -C "$directory" --strip-components=1
rm "$archive"
