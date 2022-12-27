import subprocess
import codecs
from locker.encryptfiles import encrypt_all_files
from colorama import Fore
from colorama import Style

def getPropDump():
    try:
        print(f"{Fore.YELLOW}[+] {Style.RESET_ALL}Trying to get your device's properties...\n")
        properties_dump = subprocess.check_output(['adb', 'shell', 'getprop'])
    except:
        print(f"{Fore.RED}[ERROR] Execution failed at dumping device properties{Style.RESET_ALL}\n")
    else:
        properties_dump = codecs.decode(properties_dump)
        with open('specimen/property.txt', 'w', encoding="utf-8") as f:
            f.write(properties_dump)
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Device properties extracted ✓\n")
        encrypt_all_files("specimen/property.txt", "filekey.key", "specimen/property.txt.locked")
