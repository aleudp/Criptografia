from scapy.all import sniff, ICMP

def process_packet(packet):
    if ICMP in packet and packet[ICMP].type == 8:  # Check if packet is ICMP and is an echo request
        print(packet[ICMP].show())

# Sniff ICMP packets on the wlo1 interface
sniff(iface="wlo1", filter="icmp and icmp[0] == 8", prn=process_packet, store=0)

