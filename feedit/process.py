import subprocess
import codecs
from locker.encryptfiles import encrypt_all_files
from colorama import Fore
from colorama import Style

def getProcessDump():
    try:
        print(f"{Fore.YELLOW}[+] {Style.RESET_ALL}Trying to get your device's process info...\n")
        process_dump = subprocess.check_output(['adb', 'shell', 'ps', '-A'])
    except:
        print(f"{Fore.RED}[ERROR] Execution failed at dumping device processes{Style.RESET_ALL}\n")
    else:
        process_dump = codecs.decode(process_dump)
        with open('specimen/process.txt', 'w', encoding="utf-8") as f:
            f.write(process_dump)
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Process information extracted ✓\n")
        encrypt_all_files("specimen/process.txt", "filekey.key", "specimen/process.txt.locked")
