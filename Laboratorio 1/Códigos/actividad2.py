
import sys
import time
import struct
from scapy.all import *

def send_icmp_requests(target_ip, input_text):
    characters = list(input_text)
    identifier = 1
    sequence_number = 1

    for char in characters:
        icmp_packet = IP(dst=target_ip) / ICMP(type=8, id=identifier, seq=sequence_number)
        data_field = b'#\xaa\nf\x00\x00\x00' + bytes([0x0]) + char.encode() + b'\x00' * 7 + bytes(range(0x10, 0x38))
        icmp_packet = icmp_packet / Raw(load=data_field)

        send(icmp_packet)
        sequence_number += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python icmp_sender.py <text>")
    else:
        target_ip = "8.8.8.8"  
        input_text = sys.argv[1]
        send_icmp_requests(target_ip, input_text)

sudo python3 actividad1.py "larycxpajorj h bnpdarmjm nw anmnb" 
