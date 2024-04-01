import sys
import enchant
from scapy.all import *
from termcolor import colored

def decrypt(data, corrimiento):
    decrypted = ""
    for char in data:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - ord('a') - corrimiento) % 26) + ord('a'))
            decrypted += shifted_char.upper() if char.isupper() else shifted_char
        else:
            decrypted += char
    return decrypted

def esp(palabra):
    spanish_dict = enchant.Dict("es_ES")
    return spanish_dict.check(palabra.lower())

def main(file_path):
    try:
        packets = rdpcap(file_path)
        filtered_packets = [pkt for pkt in packets if pkt.haslayer(ICMP) and pkt[IP].dst == "8.8.8.8"]

        best_shift = None
        best_decrypted_message = ""
        decrypted_messages = {}

        for corrimiento in range(26):
            decrypted_chars = []

            for pkt in filtered_packets:
                data_hex = pkt[Raw].load.hex()
                ninth_char_hex = data_hex[16:18]
                ninth_char_ascii = chr(int(ninth_char_hex, 16))
                decrypted_data = decrypt(ninth_char_ascii, corrimiento)
                decrypted_chars.append(decrypted_data)

            output = ''.join(decrypted_chars)
            decrypted_messages[corrimiento] = output

            if best_shift is None or len(output) > len(best_decrypted_message):
                best_shift = corrimiento
                best_decrypted_message = output

        for corrimiento, decrypted_message in decrypted_messages.items():
            if decrypted_message.strip().lower() == "criptografia y seguridad en redes":
                print(f"Corrimiento {corrimiento}: {colored(decrypted_message, 'green')}")
            else:
                print(f"Corrimiento {corrimiento}: {decrypted_message}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py archivo.pcapng")
    else:
        pcapng_file = sys.argv[1]
        main(pcapng_file)
