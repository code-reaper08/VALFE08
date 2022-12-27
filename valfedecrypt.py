import os
from subprocess import call
import wrap
from locker.decryptfiles import decrypt_all_files
from colorama import Fore
from colorama import Style

def valfe_decryptor():
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system("cls")
    check_count = 0
    directories = wrap.grabdir()
    print(f"""{Fore.BLUE}
  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|

 __     ___    _     _____ _____      ____                             _             
 \ \   / / \  | |   |  ___| ____|    |  _ \  ___  ___ _ __ _   _ _ __ | |_ ___  _ __ 
  \ \ / / _ \ | |   | |_  |  _| _____| | | |/ _ \/ __| '__| | | | '_ \| __/ _ \| '__|
   \ V / ___ \| |___|  _| | |__|_____| |_| |  __| (__| |  | |_| | |_) | || (_) | |   
    \_/_/   \_|_____|_|   |_____|    |____/ \___|\___|_|   \__, | .__/ \__\___/|_|   
                                                           |___/|_|                  
    {Style.RESET_ALL}""")
#     print(f"""{Fore.BLUE}
# ██    ██  █████  ██      ███████ ███████       ██████  ███████  ██████ ██████  ██    ██ ██████  ████████  ██████  ██████  
# ██    ██ ██   ██ ██      ██      ██            ██   ██ ██      ██      ██   ██  ██  ██  ██   ██    ██    ██    ██ ██   ██ 
# ██    ██ ███████ ██      █████   █████   █████ ██   ██ █████   ██      ██████    ████   ██████     ██    ██    ██ ██████  
#  ██  ██  ██   ██ ██      ██      ██            ██   ██ ██      ██      ██   ██    ██    ██         ██    ██    ██ ██   ██ 
#   ████   ██   ██ ███████ ██      ███████       ██████  ███████  ██████ ██   ██    ██    ██         ██     ██████  ██   ██ 
#     {Style.RESET_ALL}""", end=" ")
    print(f"{Fore.YELLOW}[.] {Style.RESET_ALL}Initiating VALFE-Decryptor\n")
    print(f"{Fore.YELLOW}[.] {Style.RESET_ALL}Checking whether files are intact...\n")
    if os.path.exists("specimen"):
        for entries in directories.iterdir():
            if ".locked" in str(entries):
                check_count += 1
            else:
                print(f"{Fore.YELLOW}[INFO] {Style.RESET_ALL}Files already decrypted\n")
                break
    if check_count == 7:
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Files integrity check passed!\n")
        for entries in directories.iterdir():
            print(f"Decrypting {Fore.YELLOW}[{{}}]{Style.RESET_ALL}\n".format(entries))
            decrypt_all_files(entries, "filekey.key", str(entries).strip(".locked"))
            os.remove(entries)
        os.remove("filekey.key")
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Workspace cleaned!\n")
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}All files decrypted!\n")