#!/bin/bash
for ip in $(seq 1  254); do
ping -c1 10.11.1.$ip | grep "bytes from" | cut -d" " -f4 | cut -d":" -f1 > ping_out.log &
done
