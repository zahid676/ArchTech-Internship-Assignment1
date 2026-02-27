from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

def packet_callback(packet):
    print("\n=== Packet Captured ===")
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if packet.haslayer(IP):
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

    if packet.haslayer(TCP):
        print("Protocol: TCP")
        print("Source Port:", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)

    elif packet.haslayer(UDP):
        print("Protocol: UDP")
        print("Source Port:", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)

    print("Packet Length:", len(packet))
    print("-" * 50)

print("Starting Network Sniffer...")
print("Capturing 10 packets...\n")

sniff(prn=packet_callback, count=10)
