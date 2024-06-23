from src.pcap_reader import read_pcap
from src.pcap_analyzer import extract_ips
from src.visualization import plot_ips
from src.network_utils import perform_traceroute

def main():
    pcap_file = r'C:\Users\lunch#\Documents\GitHub\PCAP_Enumeration\data\captureAll.pcap'
    packets = read_pcap(pcap_file)
    ips = extract_ips(packets)
    plot_ips(ips)
    
    target = 'www.google.com'
    traceroute_result = perform_traceroute(target)
    print(traceroute_result)

if __name__ == "__main__":
    main()
