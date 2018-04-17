#!/bin/bash

#tcpdump tcp  port 22

list=(
		http://www.sdu.edu.cn
		http://www1.scu.edu.cn
		http://www.ouc.edu.cn
		http://www.qdu.edu.cn
		http://www.sdufe.edu.cn
		http://www.sdjzu.edu.cn
		http://www.qust.edu.cn
		http://www.sdnu.edu.cn
		http://www.qfnu.edu.cn
		http://www.sdutcm.edu.cn
		http://www.bzmc.edu.cn
		http://www.hnu.edu.cn
		http://www.sdili.edu.cn
		http://www.qau.edu.cn
		http://www.ccec.edu.cn
		http://www.bztc.edu.cn
		http://www.wfmc.edu.cn
		http://www.ytu.edu.cn
		http://www.jnmc.edu.cn
		http://www.sdjtu.edu.cn
		http://www.sdut.edu.cn
		http://www.ujn.edu.cn
		http://www.ycxy.com
		http://www.lcu.edu.cn
		http://www.sdwu.edu.cn
		http://www.coscoqmc.com.cn
		http://www.qdbhu.edu.cn
		http://www.qtc.edu.cn
		)


for my_sock in $(seq 30001 31501)
do
	echo "start tcpdump"
	tcpdump -w /home/xulei/ShellFile/pcap/$my_sock.pcap > /dev/null 2> /dev/null &
	sleep 3
	echo "start ssh"
	ssh -f -n -N -D $my_sock -p 26983 root@XXXX
	sleep 5
	echo "start curl"
	web_num=$(($my_sock % 28))
	curl -L --socks5 127.0.0.1:$my_sock ${list[$web_num]}
	sleep 5
	echo "start kill tcpdump"
	ps aux|grep tcpdump | grep -v grep|awk '{print $2}'|xargs kill -9
	echo "start kill thread "$my_sock
	ps aux|grep 'ssh' | grep -v grep|awk '{print $2}'|xargs kill -9
done
	 