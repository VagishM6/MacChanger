import subprocess

# user = input("Enter user Name: ")
print("Welcome Mr.Vagish...")
command = input('Enter MAC Address: ')
network_interface = input("Enter Network Interface to Change: ")


class Change_Mac():
    def __int__(self):
        pass

    def change_mac(self, mac_input, network_interface_input):
        if len(mac_input) < 17:
            print("[-] entered character is less than 17")
        elif len(mac_input) > 17:
            print("[-] entered character is greater than 17")
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