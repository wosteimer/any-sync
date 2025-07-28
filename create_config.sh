#!/bin/bash

if [[ -f etc/client.yml ]]; then
    echo "config already exists"
    exit 0
fi

uv run make_template.py
any-sync-network create --auto
yq -iy '.storage.anyStorePath = "/anyStorage"' etc/any-sync-node-1/config.yml
yq -iy '.storage.anyStorePath = "/anyStorage"' etc/any-sync-node-2/config.yml
yq -iy '.storage.anyStorePath = "/anyStorage"' etc/any-sync-node-3/config.yml
exit 0
