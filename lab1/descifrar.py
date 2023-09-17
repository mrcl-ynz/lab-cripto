import sys
import scapy.all as scapy

def extract_icmp_payload(pcap_file):
    icmp_payload = ""
    packets = scapy.rdpcap(pcap_file)

    for packet in packets:
        if packet.haslayer(scapy.ICMP):
            icmp_data = packet[scapy.ICMP].load
            if icmp_data:
                icmp_payload += chr(icmp_data[0]) # Suponemos que el primer byte del payload contiene el caracter

    return icmp_payload

def decrypt_cesar_cipher(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('A' if char.isupper() else 'a')) - shift) % 26 + ord('A' if char.isupper() else 'a'))
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext

def main():
    if len(sys.argv) != 2:
        print("Uso: python extract_and_decrypt.py archivo.pcap")
        sys.exit(1)

    pcap_file = sys.argv[1]
    extracted_payload = extract_icmp_payload(pcap_file)

    if not extracted_payload:
        print("No se encontraron paquetes ICMP con datos.")
        sys.exit(1)

    print(f"Mensaje ICMP extraído: {extracted_payload}")

    print("Descifrando con todas las posibles claves:")
    for shift in range(26):
        decrypted_message = decrypt_cesar_cipher(extracted_payload, shift)
        print(f"Clave {shift}: {decrypted_message}")

if __name__ == "__main__":
    main()

