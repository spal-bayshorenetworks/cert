#!/bin/bash
echo "Hello"
for url in $(cat index.html | grep -o 'http[s]*://[^"]*' | cut -d'/' -f3 | sort -u)
do
host $url | grep "has address" | cut -d " " -f4
done
