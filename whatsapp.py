import httpx
from colorama import Style, Fore
import time


def check_whatsapp(number: str):
    """Check if a WhatsApp number is banned/active via Meta Web API"""
    print(f"\n{Fore.YELLOW}[*] Connecting to Meta Gateway...{Style.RESET_ALL}")
    time.sleep(1.0)

    url = f"https://api.whatsapp.com/send/?phone={number}&text&type=phone_number&app_absent=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        with httpx.Client() as client:
            response = client.get(url, headers=headers, timeout=10.0)
            html_content = response.text

        if "isn't on WhatsApp" in html_content or "is not on WhatsApp" in html_content:
            print(f"{Fore.RED}[\u2715] RESULT : BANNED OR INEXISTENT{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}Details : This number is not registered on WhatsApp servers. It has been banned or never existed.{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}[\u2713] RESULT : ACTIVE / CLEAN{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}Details : Account is active, verified and not banned.{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[!] Connection Error : {e}{Style.RESET_ALL}")
