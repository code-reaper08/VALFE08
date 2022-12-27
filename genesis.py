import os
import getpass
import specimen
import feedit.log as logger
import feedit.network as netlog
import feedit.packages as packages
import feedit.process as process
import feedit.properties as props
import feedit.service as serv
import feedit.settings as setting_fi
import locker.keygen as keygen
import locker.encryptfiles as encrypt_fi
import locker.decryptfiles as decrypt_fi
import precheck
import wrap
import valfedecrypt
from colorama import init as colorama_init
from colorama import Fore, Back
from colorama import Style

colorama_init()

print(f"\n\nWelcome to {Fore.YELLOW}VALFE08!{Style.RESET_ALL}\n")
print(f"{Fore.YELLOW}VALFE08{Style.RESET_ALL} is a android log file extraction toolkit")
print(f"""{Fore.BLUE}
██╗   ██╗ █████╗ ██╗     ███████╗███████╗ ██████╗  █████╗ 
██║   ██║██╔══██╗██║     ██╔════╝██╔════╝██╔═████╗██╔══██╗
██║   ██║███████║██║     █████╗  █████╗  ██║██╔██║╚█████╔╝
╚██╗ ██╔╝██╔══██║██║     ██╔══╝  ██╔══╝  ████╔╝██║██╔══██╗
 ╚████╔╝ ██║  ██║███████╗██║     ███████╗╚██████╔╝╚█████╔╝
  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝ ╚═════╝  ╚════╝ 
{Style.RESET_ALL}""")
print(f"Enter 1 to create new extract | Enter 2 to decrypt existing encrypted files using {Fore.BLUE}VALFE-Decryptor{Style.RESET_ALL}")
# passphrase = input()
pre_choice = int(input())
if pre_choice == 1:
    print(f"\nEnter a {Fore.YELLOW}passphrase{Style.RESET_ALL} to continue extraction {Fore.RED}[remember the passphrase][passphrase is case sensitive]{Style.RESET_ALL}")
    try:
        passphrase = getpass.getpass()
    except Exception as err:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL}\n", err)
    else:
        print(f"\n{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}Passphrase noted ✓\n")
    allfilekey_file_path = "filekey.key"
    archivekey_file_path = "archivekey.key"
    keygen.generate_key(allfilekey_file_path)
    specimen.create_specimen_container()
    decider = precheck.check_adb_devices()
    check_count_global = 0
    if decider:
        try:
            logger.getLogDump()
            check_count_global += 1
        except:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Couldn't extract device log ✖\n")
        try:
            netlog.getNetworkDump()
            check_count_global += 1
        except:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Couldn't extrat network statistics ✖\n")
        try:
            packages.getPackagesDump()
            check_count_global += 1
        except:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Couldn't extract device's package information ✖\n")
        try:
            process.getProcessDump()
            check_count_global += 1
        except:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Couldn't extract process information ✖\n")
        try:
            props.getPropDump()
            check_count_global += 1
        except:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Couldn't extract device properties ✖\n")
        try:
            serv.getServicesDump()
            check_count_global += 1
        except:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Couldn't extract information about services running ✖\n")
        try:
            setting_fi.getSettingsDump()
            check_count_global += 1
        except:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Couldn't extract device settings ✖\n")


        if check_count_global == 7:
            # wrap.checkoktozip()
            # keygen.generate_key(archivekey_file_path)
            # encrypt_fi.encrypt_all_files("specimen.tar.gz", archivekey_file_path, "specimen.tar.gz.locked")
            print(f"\n{Fore.YELLOW}[INFO] {Style.RESET_ALL}All the extracted log files are available in the {Fore.BLUE}./specimen{Style.RESET_ALL} directory and are encrypted by default")
            print(f"\n{Fore.YELLOW}[INFO] {Style.RESET_ALL}To unlock the files, please use the {Fore.BLUE}VALFE-Decryptor{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}[INFO] {Style.RESET_ALL}Enter 1 to start decrypting | enter 2 to decrypt later and exit")
            choice = int(input())
            if choice == 1:
                print(f"\nTo initiate decryption using {Fore.BLUE}VALFE-Decryptor{Style.RESET_ALL}, please enter your {Fore.YELLOW}passphrase{Style.RESET_ALL}")
                try:
                    confirm_passphrase = getpass.getpass()
                except Exception as err:
                    print("[ERROR]", err)
                else:
                    print(f"\n{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Passphrase Validation")
                if confirm_passphrase == passphrase:
                    print("\nGood to go...")
                    print(f"\nInitiating {Fore.BLUE}VALFE-Decryptor{Style.RESET_ALL}")
                    valfedecrypt.valfe_decryptor()
            else:
                print(f"\nFeel free to use {Fore.BLUE}VALFE-Decryptor{Style.RESET_ALL} later to decrypt files\n")
            print(f"Thanks for using {Fore.YELLOW}VALFE08{Style.RESET_ALL}\n")
elif pre_choice == 2:
    valfedecrypt.valfe_decryptor()
else:
    print(f"{Fore.RED}[ERROR] {Style.RESET_ALL} Not a valid input\n")


    # decrypt_fi.decrypt_all_files("specimen.tar.gz.locked", archivekey_file_path, "specimen.tar.gz")
    # wrap.unziparchive("specimen.zip", "specimen")
    # wrap.untardir()
    # os.remove("specimen.zip")

    # for entries in directory.iterdir():
    #     decrypt_fi.decrypt_all_files(entries, allfilekey_file_path, entries.strip(".locked"))
    # print("All process done!")