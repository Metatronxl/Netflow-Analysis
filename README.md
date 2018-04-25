# Netflow-Analysis

- 自动抓包脚本
- pcap文件分流

---
## pcap文件

> pcap文件头结构体

```c++

 sturct pcap_file_header
 {
      DWORD           magic;
      DWORD           version_major;
      DWORD           version_minor;
      DWORD           thiszone;
      DWORD           sigfigs;
      DWORD           snaplen;
      DWORD           linktype;
 }

```
### Descrpition

magic | version_major | version_minor | thiszone | sigfigs | snaplen | linktype
| -   | :-:           | :-:           | :-:      | :-:     | :-:     |     -:  |
32-bit | 16-bit | 16-bit| 32-bit | 32-bit|32-bit|32-bit

- **magic**：标识位（32位），这个标识位的值是16进制的 0xa1b2c3d4
- **version_major**：主版本号（16位）， 默认值为0x2
- **version_minor**:副版本号（16位），默认值为0x4
- **thiszone**：区域时间（32位），实际上该值并未使用，因此可以将该位设置为0
- **sigfigs**：精确时间戳（32位），实际上该值并未使用，因此可以将该值设置为0
- **snaplen**：数据包最大长度（32位），该值设置所抓获的数据包的最大长度，如果所有数据包都要抓获，将该值设置为65535
- **linktype**：链路层类型（32位），数据包的链路层包头决定了链路层的类型

> 以下是数据值与链路层类型的对应表
```
0            BSD       loopback devices, except for later OpenBSD
1            Ethernet, and Linux loopback devices   以太网类型，大多数的数据包为这种类型。
6            802.5 Token Ring
7            ARCnet
8            SLIP
9            PPP
10          FDDI
100        LLC/SNAP-encapsulated ATM
101        raw IP, with no link
102        BSD/OS SLIP
103        BSD/OS PPP
104        Cisco HDLC
105        802.11
108        later OpenBSD loopback devices (with the AF_value in network byte order)
113               special Linux cooked capture
114               LocalTalk
```

>packet数据包头
```c
struct pcap_pkthdr
{
struct tim         ts;
      DWORD              caplen;
      DWORD              len;
}
 
struct tim
{
DWORD       GMTtime;
DWORD       microTime
}

```
### Descrpition
GMTtime | microTime| caplen | len |
|:-:    | :-:      | :-:    |  -: |
| 32-bit |32-bit   | 32-bit | 32-bit|

- **GMT**：
- **microTime**：
- **caplen**:数据包长度(32位) ，标识所抓获的数据包保存在pcap文件中的实际长度，以字节为单位
- **len**：数据包实际长度（32位），所抓获的数据包的真实长度，如果文件中保存不是完整的数据包，那么这个值可能要比前面的数据包长度的值大



