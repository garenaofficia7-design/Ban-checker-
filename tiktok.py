import httpx
from colorama import Style, Fore
import time


def check_tiktok(username: str):
    """Check if a TikTok account is banned/active via profile lookup"""
    print(f"\n{Fore.YELLOW}[*] Checking TikTok account...{Style.RESET_ALL}")
    time.sleep(1.0)
    
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        with httpx.Client(follow_redirects=True) as client:
            response = client.get(url, headers=headers, timeout=10.0)
            html_content = response.text
            
        if response.status_code == 200 and "couldn't be found" not in html_content.lower():
            print(f"{Fore.GREEN}[✓] RESULT : ACTIVE / CLEAN{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}Details : Account is active and not banned.{Style.RESET_ALL}")
        elif response.status_code == 404 or "couldn't be found" in html_content.lower():
            print(f"{Fore.RED}[✕] RESULT : BANNED OR INEXISTENT{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}Details : This account is banned or doesn't exist.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[?] RESULT : UNAVAILABLE{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}Details : Could not determine account status (HTTP {response.status_code}).{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}[!] Connection Error : {e}{Style.RESET_ALL}")
