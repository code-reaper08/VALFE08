import os
from colorama import Fore
from colorama import Style

# print(os.getcwd() + "/specimen")
def create_specimen_container():
    if not os.path.isdir(os.getcwd()+"/specimen"):
        print(f"{Fore.YELLOW}[.] {Style.RESET_ALL}Creating a specimen directory...\n")
        os.mkdir(os.getcwd() + "/specimen")
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Specimen directory created ✓\n")
    else:
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Specimen directory found ✓\n")
