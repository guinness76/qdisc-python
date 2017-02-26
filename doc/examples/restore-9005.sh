#!/bin/bash

#connector=$1

#if [ -z "$connector" ]; then
#	echo "Specify connector (eth0 or wlan2)"
#	read connector
#fi

#sudo tc qdisc delete dev $connector parent 2:12 handle 10:
sudo tc qdisc delete dev eth0 parent 2:13 handle 10:

