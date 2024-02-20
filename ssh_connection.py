import paramiko
import os.path
import time
import sys
import re

# Ensure username/password file exists
creds_file = input("Enter the path to the credentials file (ex: /home/user/file.txt: ")

if os.path.isfile(creds_file):
    print("File loaded :)")
else:
    print(f"File {creds_file} does not exist. Exiting...")
    sys.exit()

# Ensure command file exists
commands_file = input("Enter the path to the commands file (ex: /home/user/file.txt: ")

if os.path.isfile(commands_file):
    print("File loaded :)")
else:
    print(f"File {commands_file} does not exist. Exiting...")
    sys.exit()


def ssh_connection(ip="127.0.0.1"):

    global creds_file
    global commands_file

    try:
        user_file = open(creds_file, "r")
        user_file.seek(0)
        username = user_file.readlines()[0].split(',')[0].rstrip("\n\r")
        user_file.seek(0)
        password = user_file.readlines()[0].split(',')[1].rstrip("\n\r")

        session = paramiko.SSHClient()
        # For labbing, this is fine as it will simply add host keys without question.
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # rstrip for good measure
        session.connect(ip.rstrip("\n\r"), username=username, password=password)

        # interactive shell invocation
        connection = session.invoke_shell()

        # disable pagination
        # connection.send("enable\n")
        connection.exec_command("enable\n")
        connection.exec_command("terminal length 0\n")
        time.sleep(1)

        # entering global config mode
        connection.exec_command("\n")
        connection.exec_command("configure terminal\n")
        time.sleep(1)

        # command file
        commands = open(commands_file, "r")
        commands.seek(0)

        for command in commands.readlines():
            connection.exec_command(command + '\n')
            time.sleep(2)

        user_file.close()
        commands.close()

        # max bytes that can be sent back: 65535.
        # using this to check command output for IOS syntax errors
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print(f"There was at least one ISO syntax on the following device: {ip}")
        else:
            print(f"\n Done for device: {ip}")

        # Test for reading command output
        print(str(router_output) + "\n")

        # Close connection
        connection.close()

    except paramiko.AuthenticationException:
        print("Invalid username or password in the config file or on the device.")
