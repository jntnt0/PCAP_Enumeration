import dpkt
import subprocess

class PcapReader:
    def __init__(self):
        self.interface = None
        self.capture_file = None

    def capture_traffic(self, interface, capture_file):
        """Captures network traffic using tcpdump.

        Args:
            interface: The network interface to capture traffic from (e.g., "eth0").
            capture_file: The filename to save the captured traffic (e.g., "captured_traffic.pcap").
        """
        self.interface = interface
        self.capture_file = capture_file

        command = ["tcpdump", "-i", interface, "-w", capture_file]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if error:
            print(f"Error capturing traffic: {error.decode()}")
        else:
            print(f"Traffic captured successfully to: {capture_file}")

    def read_packets(self, capture_file=None):
        """Reads packets from a PCAP file and returns a list of (timestamp, packet data) tuples.

        Args:
            capture_file: The path to the PCAP file. If not provided, uses the capture_file attribute set during capture.

        Returns:
            A list of (timestamp, packet data) tuples.
        """
        if capture_file is None:
            capture_file = self.capture_file

        if not capture_file:
            print("Error: No capture file specified.")
            return []

        packets = []
        try:
            with open(capture_file, 'rb') as f:
                pcap = dpkt.pcap.Reader(f)
                for ts, buf in pcap:
                    packets.append((ts, buf))
        except dpkt.dpkt.NeedData:
            print("Error: Need more data to process the PCAP file.")
        except ValueError as e:
            print(f"Error: {e}")
        except FileNotFoundError:
            print(f"Error: The file {capture_file} was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return packets

    def analyze_packets(self, packets):
        """Analyzes the captured packets (place your custom analysis logic here).

        This function iterates through the list of packets and performs custom analysis
        based on your specific needs. You can extract relevant information from the
        packet data (available in the second element of each tuple in the packets list).

        Args:
            packets: A list of (timestamp, packet data) tuples.
        """
        for ts, buf in packets:
            eth = dpkt.ethernet.Ethernet(buf)
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f'Timestamp: {ts}, Source IP: {ip.src}, Destination IP: {ip.dst}')

# Define the read_pcap function
def read_pcap(file_path):
    pcap_reader = PcapReader()
    return pcap_reader.read_packets(file_path)

# Example usage
if __name__ == "__main__":
    pcap_reader = PcapReader()

    # Capture traffic (optional)
    interface = "eth0"  # Replace with your network interface
    capture_file = "captured_traffic.pcap"
    pcap_reader.capture_traffic(interface, capture_file)

    # Read and analyze packets from a captured file (or provide a different filename)
    packets = pcap_reader.read_packets(capture_file)
    pcap_reader.analyze_packets(packets)
