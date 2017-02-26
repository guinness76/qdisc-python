#!/bin/bash

#connector=$1

#if [ -z "$connector" ]; then
#	echo "Specify connector (eth0 or wlan2)"
#	read connector
#fi

# Kill everything!
#sudo tc qdisc add dev $connector parent 2:12 handle 10: netem loss 100%
#sudo tc qdisc add dev lo parent 2:12 handle 10: netem loss 100%

# Base rate of 100kb, with a 650ms delay
#sudo tc qdisc add dev $connector parent 2:12 handle 10: netem delay 650ms rate 100kbit
sudo tc qdisc add dev eth0 parent 2:13 handle 10: netem delay 650ms rate 100kbit
#sudo tc qdisc add dev eth0 parent 2:13 handle 10: netem delay 300ms rate 1000kbit
