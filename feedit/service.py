import subprocess
import codecs
from locker.encryptfiles import encrypt_all_files
from colorama import Fore
from colorama import Style

def getServicesDump():
    try:
        print(f"{Fore.YELLOW}[+] {Style.RESET_ALL}Trying to get all the services running in your device...\n")
        services_dump = subprocess.check_output(['adb', 'shell', 'service', 'list'])
    except:
        print(f"{Fore.RED}[ERROR] Execution failed at gathering all running services{Style.RESET_ALL}\n")
    else:
        services_dump = codecs.decode(services_dump)
        with open('specimen/services.txt', 'w', encoding="utf-8") as f:
            f.write(services_dump)
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Running services information extracted ✓\n")
        encrypt_all_files("specimen/services.txt", "filekey.key", "specimen/services.txt.locked")

