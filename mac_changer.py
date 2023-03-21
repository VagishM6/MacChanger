import subprocess
import socket

user = input("User Name > ")
print(f"Welcome {format(user)}...")

command = input('Enter MAC Address > ')
network_interface = input("Enter Network Interface to change > ")

interface_list = ["eth0", "wlan0"]


class Change_Mac():
    def __int__(self):
        pass

    def change_mac(self, mac_input, network_interface_input):
        if len(mac_input) < 17:
            print("[-] entered characters are less than 17")
        elif len(mac_input) > 17:
            print("[-] entered characters are greater than 17")
        elif network_interface_input == "":
            print("[-] Network Interface Device has not been provided")
        elif network_interface_input not in interface_list:
            print("[-] Provided interface is Invalid")
        else:
            subprocess.call(f"ifconfig {format(network_interface_input)} down", shell=True)
            subprocess.call(f"ifconfig {format(network_interface_input)} hw ether {format(mac_input)}", shell=True)
            subprocess.call(f"ifconfig {format(network_interface_input)} up", shell=True)
            print(f'[+] MAC Address Changed to {format(mac_input)}, for network interface: ' + network_interface_input)

class Main():
    run_command = Change_Mac()
    run_command.change_mac(command, network_interface)


if __name__ == '__main__':
    Main()