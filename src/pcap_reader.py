import dpkt

def read_pcap(file_path):
    with open(file_path, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        packets = [(ts, buf) for ts, buf in pcap]
    return packets
