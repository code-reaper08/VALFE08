import subprocess
import codecs
from locker.encryptfiles import encrypt_all_files
from colorama import Fore
from colorama import Style

def getPackagesDump():
    try:
        print(f"{Fore.YELLOW}[+] {Style.RESET_ALL}Trying to get information on all packages in your device...\n")
        package_dump = subprocess.check_output(['adb', 'shell', 'pm', 'list', 'packages', '-f'])
    except:
        print(f"{Fore.RED}[ERROR] Execution failed at dumping all package information{Style.RESET_ALL}\n")
    else:
        package_dump = codecs.decode(package_dump)
        with open('specimen/package.txt', 'w', encoding="utf-8") as f:
            f.write(package_dump)
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Package information extracted ✓\n")
        encrypt_all_files("specimen/package.txt", "filekey.key", "specimen/package.txt.locked")