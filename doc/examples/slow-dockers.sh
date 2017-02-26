#!/bin/bash

#connector=$1

#if [ -z "$connector" ]; then
#	echo "Specify connector (eth0 or wlan1)"
#	read connector
#fi

#sudo tc qdisc add dev $connector parent 1:11 handle 10: netem loss 100%

# Kill everything!
#sudo tc qdisc add dev lo parent 2:12 handle 30: netem loss 100%


# Base rate of 100kb, with a 300ms delay
#sudo tc qdisc add dev lo parent 2:12 handle 30: netem delay 650ms rate 100kbit
#sudo tc qdisc add dev lo parent 2:12 handle 30: netem delay 100ms 650ms 1% loss 50%
sudo tc qdisc add dev eth0 parent 2:12 handle 30: netem delay 10ms 400ms 10% loss 1% 25%
