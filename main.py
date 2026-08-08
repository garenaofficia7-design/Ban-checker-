from colorama import Fore, Style, init
import sys
import os
from handlers.whatsapp import check_whatsapp
from handlers.facebook import check_facebook
from handlers.twitter import check_twitter
from handlers.instagram import check_instagram
from handlers.tiktok import check_tiktok
from handlers.telegram import check_telegram
from handlers.telegram2 import check_telegram_phone
from handlers.discord import check_discord
from handlers.snapchat import check_snapchat


init(autoreset=True)

RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.LIGHTGREEN_EX
MAGENTA = Fore.MAGENTA
BLACK  = Fore.LIGHTBLACK_EX
YELLOW = Fore.LIGHTYELLOW_EX
CYAN = Fore.CYAN

VERSION = 1.0
AUTHORS = "SavageHackZz"


def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def logo():
    print(f"""{RED}
    ███████╗ █████╗ ██╗   ██╗ █████╗  ██████╗ ███████╗██╗  ██╗ █████╗  ██████╗██╗  ██╗
    ██╔════╝██╔══██╗██║   ██║██╔══██╗██╔════╝ ██╔════╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝
    ███████╗███████║██║   ██║███████║██║  ███╗█████╗  ███████║███████║██║     █████╔╝
    ╚════██║██╔══██║╚██╗ ██╔╝██╔══██║██║   ██║██╔══╝  ██╔══██║██╔══██║██║     ██╔═██╗
    ███████║██║  ██║ ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║  ██║██║  ██║╚██████╗██║  ██╗
    ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

                                                                        Version : {VERSION}
                                                                        Check ban Platform
                                                                        Author: {AUTHORS}
""")


def menu():
    clear()
    logo()
    print(f" {RED}[ {BLACK}1 {RED}]{BLACK}  WHAT{RED}SAPP    {RED}[ {BLACK}2 {RED}]{BLACK}  FACE{RED}BOOK")
    print(f" {RED}[ {BLACK}3 {RED}]{BLACK}  TWI{RED}TER      {RED}[ {BLACK}4 {RED}]{BLACK}  INSTA{RED}GRAM")
    print(f" {RED}[ {BLACK}5 {RED}]{BLACK}  TIK{RED}TOK      {RED}[ {BLACK}6 {RED}]{BLACK}  TELE{RED}GRAM")
    print(f" {RED}[ {BLACK}7 {RED}]{BLACK}  DIS{RED}CORD     {RED}[ {BLACK}8 {RED}]{BLACK}  SNAP{RED}CHAT")
    print(f" {RED}[ {BLACK}9 {RED}]{BLACK}  TELEGRAM PH{RED}ONE")
    print(f" {RED}[ {BLACK}0 {RED}]{BLACK}  QU{RED}IT")


def main():
    while True:
        menu()
        try:
            choose = int(input(f"\n\n {RED} SavageHack@root/home {BLACK}~#>>  "))
        except ValueError:
            print(f"{RED}[!] Invalid input. Please enter a number.{Style.RESET_ALL}")
            input(f"{YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            continue
        except KeyboardInterrupt:
            print(f"{RED} Existing...... Good Bye !")
            break

        if choose == 1:
            number = input(f"\n{RED} Enter WhatsApp number...\n{RED} SavageHack@root/home{BLACK}/whatsapp >> ")
            check_whatsapp(number)
            input(f"\n{YELLOW}Press Enter to continue...{Style.RESET_ALL}")

        elif choose == 2:
            username = input(f"\n{RED} Enter Facebook username...\n{RED} SavageHack@root/home{BLACK}/facebook >> ")
            check_facebook(username)
            input(f"\n{YELLOW}Press Enter to continue...{Style.RESET_ALL}")

        elif choose == 3:
            username = input(f"{RED} Enter Twitter/X username...\n{RED} SavageHack@root/home{BLACK}/twitter >> ")
            check_twitter(username)
            input(f"\n{YELLOW}Press Enter to continue...{Style.RESET_ALL}")

        elif choose == 4:
            username = input(f"{RED} Enter Instagram username...\n{RED} SavageHack@root/home{BLACK}/instagram >> ")
            check_instagram(username)
            input(f"\n{YELLOW}Press Enter to continue...{Style.RESET_ALL}")

        elif choose == 5:
            username = input(f"{RED} Enter TikTok username...\n{RED} SavageHack@root/home{BLACK}/tiktok >> ")
            check_tiktok(username)
            input(f"\n{YELLOW}Press Enter to continue...{Style.RESET_ALL}")

        elif choose == 6:
            username = input(f"{RED} Enter Telegram username (with or without @)...\n{RED} SavageHack@root/home{BLACK}/telegram >> ")
            check_telegram(username)
            input(f"\n{YELLOW}Press Enter to continue...{Style.RESET_ALL}")

        elif choose == 7:
            user_id = input(f"{RED} Enter Discord User ID...\n{RED} SavageHack@root/home{BLACK}/discord >> ")
            check_discord(user_id)
            input(f"\n{YELLOW}Press Enter to continue...{Style.RESET_ALL}")

        elif choose == 8:
            username = input(f"{RED} Enter Snapchat username...\n{RED} SavageHack@root/home{BLACK}/snapchat >> ")
            check_snapchat(username)
            input(f"\n{YELLOW}Press Enter to continue...{Style.RESET_ALL}")

        elif choose == 9:
            number = input(f"{RED} Enter Telegram phone number (with country code, e.g. +33612345678)...\n{RED} SavageHack@root/home{BLACK}/telegram2 >> ")
            check_telegram_phone(number)
            input(f"\n{YELLOW}Press Enter to continue...{Style.RESET_ALL}")

        elif choose == 0:
            print(f"\n{GREEN}Exiting... Goodbye!{Style.RESET_ALL}")
            break

        else:
            print(f"{RED}[!] Invalid option. Choose 0-9.{Style.RESET_ALL}")
            input(f"{YELLOW}Press Enter to continue...{Style.RESET_ALL}")


main()
