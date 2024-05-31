#!/bin/bash

# Input domain name  
domain="$1"
# Query crt.sh and extract unique domain names  
:
clear
rm domain.txt
rm host.txt
rm info.txt
curl -s "https://crt.sh/?q=%25.$domain&output=json" | jq -r '.[].name_value' | sort -u >> domain.txt;
cat domain.txt | while read target; do host $target | awk '/has address/ {print $4}' >> host.txt; done
cat host.txt | while read address; do curl -s ipinfo.io/$address | jq '"\n".hostname, .region, .timezone' >> info.txt; done

