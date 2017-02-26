#!/bin/bash

#connector=$1

#if [ -z "$connector" ]; then
#	echo "Specify connector (eth0 or wlan1)"
#	read connector
#fi

#sudo tc qdisc delete dev $connector root
sudo tc qdisc delete dev eth0 root
