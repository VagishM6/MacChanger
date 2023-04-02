import subprocess
import optparse
import re

# Usage
# python3 mac_changer_original.py -i [interface name] -m [MAC address]


class Change_Mac():
    def __int__(self):
        pass

    def get_list(self):
        interface_list = ["eth0", "wlan0"]
        return interface_list

    def change_mac(self, mac_input, network_interface_input):
        if len(mac_input) < 17:
            print("[-] entered characters are less than 17")
        elif len(mac_input) > 17:
            print("[-] entered characters are greater than 17")
        elif network_interface_input == "":
            print("[-] Network Interface Device has not been provided")
        elif network_interface_input not in self.get_list():
            print("[-] Provided interface is Invalid")
        else:
            # subprocess.call(f"ifconfig {format(network_interface_input)} down", shell=True)
            # subprocess.call(f"ifconfig {format(network_interface_input)} hw ether {format(mac_input)}", shell=True)
            # subprocess.call(f"ifconfig {format(network_interface_input)} up", shell=True)

            subprocess.call(["ifconfig", network_interface_input, "down"])
            subprocess.call(["ifconfig", network_interface_input, "hw", "ether", mac_input])
            subprocess.call(["ifconfig", network_interface_input, "up"])

            print(f'[+] MAC Address Changed to {format(mac_input)}, for network interface: ' + network_interface_input)

    def get_arguments(self):
        parser = optparse.OptionParser()
        parser.add_option("-i", "--interface", dest="interface", help="input the interface name")
        parser.add_option("-m", "--mac", dest="mac_address", help="enter the MAC address to change")
        return parser.parse_args()


class Main():

        try:
            run_command = Change_Mac()
            (options, args) = run_command.get_arguments()
            command = options.mac_address
            network_interface = options.interface

            run_command.change_mac(command, network_interface)

            check_out = subprocess.check_output(["ifconfig", options.interface])
            # print(check_out)
            result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", check_out.decode("utf-8"))
            # print("Result: " + result.group(0))

            if result.group(0) == options.mac_address:
                print("< MAC address successfully changed >")
            else:
                print("MAC address has not been changed...")
        except:
            print("Required Arguments not provided")


if __name__ == '__main__':
    Main()
