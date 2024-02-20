import sys
import subprocess

def ip_ping(devices):
    '''For each address in the supplied list, we attemt to ping it.
    The standard output and errors are sent to devnull as we do not care about them.
    We capture the reply type (https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) and check if type is 0...reachable'''
    for ip in devices:
        ip = ip.rstrip("\n\r")
        ping_reply = subprocess.call(['ping', '-c', '2', ip,], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if ping_reply == 0:
            print(f"{ip} is reachable")
            continue
        else: print(f"{ip} is not reachable. There may be an issue with ....... the network")
        sys.exit()

if __name__ == "__main__":
    # for testing
    # devices = ['8.8.8.8', '1.1.1.1', '10.10.10.10', '192.444.555.666']
    ip_ping(devices)
