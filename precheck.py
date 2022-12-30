import subprocess
import platform
from colorama import Fore
from colorama import Style

def precheck():
    info_list = []
    valid = False
    operating_system  = platform.system() + " " + platform.release()
    info_list.append(operating_system)
    try:
        adb_version = subprocess.check_output(['adb', '--version'])
    except subprocess.CalledProcessError as catcherr:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL}\n", catcherr.returncode, catcherr.output)
        print(f"{Fore.GREEN}[INFO] {Style.RESET_ALL} Please install ADB to use VALFE08.")
        print(f"{Fore.GREEN}[INFO] {Style.RESET_ALL} Know more about VALFE08's prerequisites from https://github.com/code-reaper08/VALFE08#requirements")
        valid = False
    else:
        valid = True
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}ADB installation detected ✓\n")
        adb_version = adb_version.decode('ASCII')
        print(f"{Fore.YELLOW}----------------------------------------------------------------{Style.RESET_ALL}\n")
        print(adb_version)
        print(f"{Fore.YELLOW}----------------------------------------------------------------{Style.RESET_ALL}\n")
    finally:
        info_list.append(valid)
    if valid:
        return info_list

def check_adb_devices():
    validity_check = precheck()[1]
    print(f"{Fore.YELLOW}[+] {Style.RESET_ALL}Checking connected devices...\n")
    if validity_check:
        try:
            adb_devices = subprocess.check_output(['adb', 'devices', '-l'])
        except subprocess.CalledProcessError as catcherr:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL}\n", catcherr.returncode, catcherr.output)
        else:
            adb_devices = adb_devices.decode('ASCII')
            if len(adb_devices) > 28:
                print(f'{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Below Devices detected\n')
                print(f"{Fore.YELLOW}----------------------------------------------------------------{Style.RESET_ALL}\n")
                print(adb_devices)
                print(f"{Fore.YELLOW}----------------------------------------------------------------{Style.RESET_ALL}\n")
            else:
                print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}No devices found\n")
                print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Connect your device using USB, to start extraction\n")
                
    if validity_check and len(adb_devices) > 28:
        return True
    else:
        return False