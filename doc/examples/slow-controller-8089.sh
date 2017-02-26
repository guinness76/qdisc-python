#!/bin/bash

#connector=$1

#if [ -z "$connector" ]; then
#	echo "Specify connector (eth0 or wlan2)"
#	read connector
#fi

# Kill everything!
#sudo tc qdisc add dev $connector parent 2:14 handle 20: netem loss 100%
#sudo tc qdisc add dev lo parent 2:14 handle 20: netem loss 100%

# Base rate of 100kb, with a 650ms delay
#sudo tc qdisc add dev $connector parent 2:14 handle 20: netem delay 650ms rate 100kbit
#sudo tc qdisc add dev lo parent 2:14 handle 20: netem delay 650ms rate 100kbit
sudo tc qdisc add dev eth0 parent 2:14 handle 20: netem delay 10ms 5000ms 1% loss 50%
