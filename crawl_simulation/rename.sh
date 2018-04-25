#!/bin/bash
	#
	# Author: Gihan De Silva @  gihansblog.com
	# rename script
	# rename.sh
	clear
	x=0
	for i in `ls *.pcap`
	do
	x=`expr $x + 1`
	mv $i SSH_172_96_224_205_HTTP_$x.pcap
	done



	echo “rename done!”