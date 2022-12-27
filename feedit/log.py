import subprocess
import codecs
from locker.encryptfiles import encrypt_all_files
from colorama import Fore
from colorama import Style

def getLogDump():
    try:
        print(f"{Fore.YELLOW}[+]{Style.RESET_ALL} Trying to get your device's log info...\n")
        log_dump = subprocess.check_output(['adb', 'logcat', '-d', '-b', 'all', '*:V'])
    except:
        print(f"{Fore.RED}[ERROR] Execution failed at producing log dump{Style.RESET_ALL}\n")
    else:
        log_dump = codecs.decode(log_dump)
        with open('specimen/log.txt', 'w', encoding="utf-8") as f:
            f.write(log_dump)
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Log information extracted ✓\n")
        encrypt_all_files("specimen/log.txt", "filekey.key", "specimen/log.txt.locked")