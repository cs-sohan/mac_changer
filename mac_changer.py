#! /usr/bin/env/python

import subprocess  # This module is used to run system commands
import optparse  # This module is used to take inline-arguments from users
import re  # This module is used to for regular expression


def get_arguments():  # Function to take arguments from the user
    parser = optparse.OptionParser()  # Object of OptionParser Class
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac", dest="newMac", help="New Mac Address")
    (parserOptions, parserArguments) = parser.parse_args()  # storing the result of parse_args function to variables
    if not parserOptions.interface:
        parser.error("[-] Please specify interface, refer --help for more info")
    if not parserOptions.newMac:
        parser.error("[-] Please specify MAC Address, refer --help for more info")
    return parserOptions  # returning options fetched from the user


def mac_change(interface, newMac):  # Function to change mac address
    if interface is not None and newMac is not None:
        print("[+] Changing MAC Address")
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
        subprocess.call(["ifconfig", interface, "up"])
        print("[+] Mac Address changed successfully")


def get_current_mac(interface):
    if interface is not None:
        interface_config_result = subprocess.check_output(["ifconfig", interface]).decode(
            "utf-8")  # storing ifconfig/ipconfig result
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interface_config_result)    #checking regular expression
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("[-] Could not read MAC Address")
    else:
        return None


options = get_arguments()  # getting user arguments via get_arguments function
current_mac = get_current_mac(options.interface)    # Getting current mac address
if current_mac is not None:
    print("[+] Current Mac: " + current_mac)
else:
    print("[+] Unable to fetch current MAC Address")
mac_change(options.interface, options.newMac)   # Function to change mac address
current_mac = get_current_mac(options.interface)    # Getting current mac address
if current_mac == options.newMac:
    print("[+] MAC Address changed successfully to " + str(current_mac))
elif current_mac is None:
    print("[-] Could not change MAC Address")
else:
    print("[-] Could not change MAC Address")
