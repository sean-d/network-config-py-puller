import os.path

def validate_ip_file():
    '''Validates if the user-supplied file containing the IPs of the devices is valid'''
    ip_file = input("\n# Enter the path to the asset file (ex: /home/user/file.txt): ")

    if os.path.isfile(ip_file): print("\n* IP file is valid :) \n")
    else:
        print(f"\n* {ip_file} not found. Try again.")
        ip_file = input("\n# Enter the path to the asset file (ex: /home/user/file.txt): ")

    with open(ip_file, "r") as selected_ip_file:
        selected_ip_file.seek(0)
        ip_list = selected_ip_file.readlines()
        print(ip_list)

    return ip_list

if __name__ == "__main__":
    validate_ip_file()
