import unittest
from src.pcap_reader import read_pcap

class TestPcapReader(unittest.TestCase):
    def test_read_pcap(self):
        packets = read_pcap('data/sample.pcap')
        self.assertTrue(len(packets) > 0)

if __name__ == '__main__':
    unittest.main()
