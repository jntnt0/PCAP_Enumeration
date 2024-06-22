import dpkt

def extract_ips(packets):
    ips = []
    for ts, buf in packets:
        eth = dpkt.ethernet.Ethernet(buf)
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            ips.append((ip.src, ip.dst))
    return ips
