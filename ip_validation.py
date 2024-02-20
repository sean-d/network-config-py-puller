import sys


def check_ip(device_list):
    '''Octets are cast to int since they are str in the list.

        We check to ensure that each IP in the file adheres to the following:
        1. 4 octets in length
        2. the first octet is between 1 and 223 as 224-239 are for multicast
        and 240 and up are reserved for future use
        3. the first octet is is not 127 (loopback)
        4. the first 2 octets are not 169.254 (link-local)...if the address is 169 and 254, we have... false OR false which is false and will cause the if to fail
        5. octets 2,3,4 are 0-254'''

    for ip in device_list:
        ip = ip.rstrip("\n\r")
        in_octets = ip.split(".")


        if (len(in_octets) == 4) \
            and (int(in_octets[0]) != 127) \
            and ((int(in_octets[0]) != 169 or int(in_octets[1]) != 254)) \
            and (1 <= int(in_octets[0]) <= 223) \
            and (0 <= int(in_octets[1]) <= 254) \
            and (0 <= int(in_octets[2]) <= 254) \
            and (0 <= int(in_octets[3]) <= 254):
            print(f"valid: {in_octets}")
            continue
        else:
            print(f"** There is an invalid address: {in_octets}")
            sys.exit()

if __name__ == "__main__":
    #for testing
    device_list = ['172.16.90.2\n', '172.16.90.3\n', '172.16.90.4\n', "1.254.255.254", "1.24.24.255", "255.1.1.1", '169.254.1.1\n', '10.254.1.1', "1.254.255.254", "1.24.24.255", "255.1.1.1", '169.1.1.1', '127.0.0.1', "10.10", "0.1.2.3", "1.255.254.254"]
    check_ip(device_list)
