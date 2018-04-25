import sys
import struct
import os
import random
import traceback


def write_pcap(pcap_header_string,tuple_info,file_name,pcap_dir):
    num = 0
    file_path = pcap_dir+"/"+file_name
    if os.path.exists(file_path):
        file_path = file_path +'_2'
    os.mkdir(file_path)
    for key in tuple_info:
        finap = open(file_path+"/"+file_name+"-"+key+".pcap","wb")
        finap.write(pcap_header_string+tuple_info[key])
        finap.close()
        num+=1

def read_pcap(filedir,pcap_dir):
    i = 24
    tuple_info = {}
    pcap_num = 0
    fpcap = open(filedir,"rb")
    string_data = fpcap.read()

    file_middle_name = filedir.split("/")[-1] # get file name
    file_name = file_middle_name.split(".")[0]

    pcap_header_string = string_data[0:24]
    while(i<len(string_data)):
        pcap_packet_header = string_data[i:i+16]
        pcap_packet_header_len = string_data[i+12:i+16]
        packet_len = struct.unpack('I',pcap_packet_header_len)[0]
        packet_value = string_data[i+16:i+16+packet_len]
        i = i+ packet_len+16

        sip = packet_value[26:30]
        sip_str = str(sip[0]) + "." + str(sip[1]) + "." + str(sip[2]) + "." + str(sip[3])
        dip = packet_value[30:34]
        dip_str = str(dip[0]) + "." + str(dip[1]) + "." + str(dip[2]) + "." + str(dip[3])
        sport = packet_value[34:36]
        sport_str = str(sport[0]*256 + sport[1])
        dport = packet_value[36:38]
        dport_str = str(dport[0]*256 + dport[1])
        tuple_string = sip_str + "_" + sport_str + "-" + dip_str + "_" + dport_str        ## 正反四元组
        tuple_contrary_string = dip_str + "_" + dport_str + "-" + sip_str + "_" + sport_str

        if tuple_string in tuple_info:     ## 将相同的数据合并成为一条流
            tuple_info[tuple_string] += pcap_packet_header + packet_value
        elif tuple_contrary_string in tuple_info:
            tuple_info[tuple_contrary_string] += pcap_packet_header + packet_value
        else:
            tuple_info[tuple_string] = pcap_packet_header + packet_value

    write_pcap(pcap_header_string, tuple_info, file_name, pcap_dir)

def is_contain_file(pcap_path):
    flag = 0
    for item in pcap_path:
        if item.endswith(".pcap"):
            flag = 1
            break
    return flag


def pcapFunc():
    try:
        pcap_dir = sys.argv[1]
    except:
        print("input a parameter of pcap directory")
        sys.exit(1)

    if os.path.isdir(pcap_dir):
        files = os.listdir(pcap_dir)
        if is_contain_file(files) == 1:
            for item in files:
                if item.endswith(".pcap"):
                    read_pcap(pcap_dir+"/"+item,pcap_dir)
        else:
            print("the directory does not contain any pcap file!")
            sys.exit(0)
    elif pcap_dir.endswith(".pcap"):
        if os.path.exists(pcap_dir):
            read_pcap(pcap_dir,"/".join(pcap_dir.split("/")[:-1]))
        else:
            print("Error! the pcap is not exit please check it!")
            exit(2)
    else:
        print("Error! the directory is not true please check it!")
        sys.exit(1)

if __name__ == '__main__':
    pcapFunc()








