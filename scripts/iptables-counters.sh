#!/bin/bash

# Reset all counters and iptables rules
iptables -Z && iptables -F

# Measure incoming traffic from 10.11.1.220
iptables -I INPUT 1 -s 10.11.1.220 -j ACCEPT

# Measure outgoing traffic to 10.11.1.220
iptables -I OUTPUT 1 -d 10.11.1.220 -j ACCEPT

