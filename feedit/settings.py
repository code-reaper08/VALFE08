import subprocess
import codecs
from locker.encryptfiles import encrypt_all_files
from colorama import Fore
from colorama import Style

def getSettingsDump():
    try:
        print(f"{Fore.YELLOW}[+] {Style.RESET_ALL}Trying to get your device settings...\n")
        settings_dump = subprocess.check_output(['adb', 'shell', 'cmd', 'settings', 'list', 'global'])
    except:
        print(f"{Fore.RED}[ERROR] Execution failed at gathering device's settings{Style.RESET_ALL}\n")
    else:
        settings_dump = codecs.decode(settings_dump)
        with open('specimen/settings.txt', 'w', encoding="utf-8") as f:
            f.write(settings_dump)
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Device settings extracted ✓\n")
        encrypt_all_files("specimen/settings.txt", "filekey.key", "specimen/settings.txt.locked")
