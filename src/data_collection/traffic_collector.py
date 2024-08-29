from scapy.all import sniff

def collect_network_traffic(interface, count):
    """Collect network traffic data using Scapy."""
    packets = sniff(iface=interface, count=count)
    return packets

if __name__ == "__main__":
    packets = collect_network_traffic('en0', 100)
    print(f"Collected {len(packets)} packets")