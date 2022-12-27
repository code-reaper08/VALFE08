import subprocess
import codecs
from locker.encryptfiles import encrypt_all_files
from colorama import Fore
from colorama import Style

def getNetworkDump():
    try:
        print(f"{Fore.YELLOW}[+] {Style.RESET_ALL}Trying to get network statistics from your device...\n")
        network_dump = subprocess.check_output(['adb', 'shell', 'netstat', '-W'])
    except:
        print(f"{Fore.RED}[ERROR] Execution failed at producing network statistics using ADB{Style.RESET_ALL}\n")
    else:
        network_dump = codecs.decode(network_dump)
        with open('specimen/network.txt', 'w', encoding="utf-8") as f:
            f.write(network_dump)
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Network statistics extracted ✓\n")
        encrypt_all_files("specimen/network.txt", "filekey.key", "specimen/network.txt.locked")