import asyncio
from telethon import TelegramClient
from telethon.errors import PhoneNumberBannedError, PhoneNumberInvalidError, FloodWaitError
from colorama import Fore, Style
from config import API_ID, API_HASH


async def check_telegram_ban(numero: str):
    """
    Vérifie si un numéro est banni de Telegram en tentant de demander un code.
    """
    print(f"\n{Fore.YELLOW}[*] Connecting to Telegram MTProto Servers...{Style.RESET_ALL}")
    
    # Création du client (crée un fichier .session en local)
    client = TelegramClient('savage_check_session', API_ID, API_HASH)
    
    try:
        await client.connect()
        
        # Tentative d'envoi de code (méthode de détection)
        await client.send_code_request(numero)
        
        print(f"{Fore.GREEN}[✓] RESULT : ACTIVE / CLEAN{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}Details : This number is registered and NOT banned.{Style.RESET_ALL}")

    except PhoneNumberBannedError:
        print(f"{Fore.RED}[✕] RESULT : BANNED{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}Details : This phone number is permanently banned from Telegram.{Style.RESET_ALL}")

    except PhoneNumberInvalidError:
        print(f"{Fore.RED}[!] RESULT : INVALID NUMBER{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}Details : The format is incorrect or the number doesn't exist.{Style.RESET_ALL}")

    except FloodWaitError as e:
        print(f"{Fore.MAGENTA}[!] RATE LIMIT : FLOOD WAIT{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}Details : Too many requests. Please wait {e.seconds} seconds.{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[!] SYSTEM ERROR : {e}{Style.RESET_ALL}")

    finally:
        await client.disconnect()

def check_telegram_phone(numero: str):
    """
    Fonction synchrone pour vérifier un numéro Telegram (wrapper pour le menu).
    """
    asyncio.run(check_telegram_ban(numero))
