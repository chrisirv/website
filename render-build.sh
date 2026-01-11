#!/usr/bin/env bash

# Exit on error
set -o errexit

# Define the version we need
HUGO_VERSION=0.146.0

# Download Hugo Extended from GitHub
wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz
tar -xf hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz

# Run our newly downloaded Hugo binary
./hugo --gc --minify
