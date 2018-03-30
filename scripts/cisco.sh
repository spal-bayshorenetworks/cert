#!/bin/bash
echo "Hello"
for url in $(grep -o '[a-zA-Z0-9_\.-]*\.*cisco\.com' index.html | sort -u)
do
host $url | grep "has address" | cut -d " " -f4
done

