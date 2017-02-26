#!/bin/bash

#connector=$1

#if [ -z "$connector" ]; then
#	echo "Specify connector (eth0 or wlan1)"
#	read connector
#fi

#Creation of the root of the tree
#sudo tc qdisc add dev $connector handle 1: root htb
sudo tc qdisc add dev eth0 handle 2: root htb

#Then, we create the default root class which will be used by traffic not concerned by any rules
#sudo tc class add dev $connector parent 1: classid 1:1 htb rate 1000Mbps
sudo tc class add dev eth0 parent 2: classid 2:1 htb rate 1000Mbps

#Then, we create children classes. Each child can provide a different type of delay behavior. Filters use 1:11|1:12|1:13 in their parameters to determine which child to target.

# Rule to kill the docker ports on the connector
#sudo tc class add dev $connector parent 1:1 classid 1:11 htb rate 100Mbps

# Rule to modify the docker ports on local loopback
sudo tc class add dev eth0 parent 2:1 classid 2:12 htb rate 100Mbps

# Rule to modify port 8088
sudo tc class add dev eth0 parent 2:1 classid 2:13 htb rate 100Mbps

# Rule to modify port 8089
sudo tc class add dev eth0 parent 2:1 classid 2:14 htb rate 100Mbps

# Port filters
sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip dport 9000 0xffff flowid 2:12
sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip dport 9001 0xffff flowid 2:12
sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip dport 9002 0xffff flowid 2:12
sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip dport 9003 0xffff flowid 2:12
sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip dport 9004 0xffff flowid 2:12
#sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip sport 9005 0xffff flowid 2:13
#sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip dport 9005 0xffff flowid 2:13
sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip src 10.20.6.32 flowid 2:13
sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip dst 10.20.6.32 flowid 2:13
sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip sport 8089 0xffff flowid 2:14
sudo tc filter add dev eth0 protocol ip prio 1 u32 match ip dport 8089 0xffff flowid 2:14

# Note: for these tests to work properly, the controller must make outgoing connections to the docker agents.
# Also: Chrome seems to use localhost 8088 in some strange way that bypasses the tc system. When testing with Chrome, use the IP address instead of localhost. Or use Firefox.
