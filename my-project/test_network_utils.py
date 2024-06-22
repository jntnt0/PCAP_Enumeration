from scapy.all import *

def perform_traceroute(target):
    result, _ = traceroute(target, maxttl=20)
    return result
