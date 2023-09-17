import sys
from scapy.all import *

def enviar_paquete_icmp(dest_ip, identificador, mensaje):
    paquetes = []
    secuencia = 1

    for caracter in mensaje:
        payload = caracter.encode()  # Convierte el caracter en bytes
        payload += secuencia.to_bytes(2, byteorder='little')  # Agrega secuencia en little-endian (2 bytes)
        payload += b'\x00\x00\x00\x00\x00'  # Agrega 5 bytes en 0x00
        payload += bytes(range(0x10, 0x38))  # Agrega bytes de 0x10 a 0x37

        paquete = IP(dst=dest_ip) / ICMP(id=identificador, seq=secuencia) / payload
        paquetes.append(paquete)
        secuencia += 1

    for paquete in paquetes:
        send(paquete)

if len(sys.argv) != 2:
    print("Uso: python enviar_icmp.py <mensaje>")
    sys.exit(1)

mensaje = sys.argv[1]
identificador = 12345  # Identificador distinto de 0
dest_ip = "8.8.8.8"  # Dirección IP de destino

enviar_paquete_icmp(dest_ip, identificador, mensaje)
