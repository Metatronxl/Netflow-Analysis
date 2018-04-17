#!/bin/bash

#tcpdump tcp  port 22
for my_sock in $(seq 30001 31501)
do
	echo "start tcpdump"
	tcpdump -w /home/xulei/ShellFile/pcap/$my_sock.pcap > /dev/null 2> /dev/null &
	sleep 3
	echo "start ssh"
	ssh -f -n -N -D $my_sock -p port root@xxx.xxx.xxx.xxx
	sleep 5
	echo "start curl"
	curl -L --socks5 127.0.0.1:$my_sock http://www1.scu.edu.cn/
	sleep 5
	echo "start kill tcpdump"
	ps aux|grep tcpdump | grep -v grep|awk '{print $2}'|xargs kill -9
	echo "start kill thread "$my_sock
	ps aux|grep 'ssh' | grep -v grep|awk '{print $2}'|xargs kill -9
done
	 