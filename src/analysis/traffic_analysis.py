from scapy.all import TCP

def analyze_traffic(packets):
    # Example analysis: Count TCP packets
    tcp_count = 0
    for packet in packets:
        if packet.haslayer(TCP):
            tcp_count += 1
    print(f'TCP Packet Count: {tcp_count}')