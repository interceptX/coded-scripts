#!/bin/bash

# Input domain name  
domain="mcgi.org"

# Query crt.sh and extract unique domain names  
curl -s "https://crt.sh/?q=%25.$domain&output=json" | jq -r '.[].name_value' | sort -u
