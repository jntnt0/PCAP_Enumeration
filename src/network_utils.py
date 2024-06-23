from scapy.all import *
from scapy.layers.inet import traceroute

def perform_traceroute(target):
    result, _ = traceroute(target, maxttl=20)
    return result
