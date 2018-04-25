#!/bin/bash
for ip in $(seq 1 254); do host 10.11.1.$ip; done | column -t
