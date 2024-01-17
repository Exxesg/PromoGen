#╔═════════════════════════════════════════════════════╗
#║    || - ||        Code By Jimo            || - ||   ║
#╚═════════════════════════════════════════════════════╝

import os
import time
import tls_client
import uuid
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
from datetime import datetime
from threading import Lock
from traceback import print_exc
from random import choice

os.system("cls && title Promo Gen By Jimo | .gg/LowCost")


lock = Lock()
genned = 0

class Logger:
    @staticmethod
    def Sprint(tag: str, content: str, color):
        ts = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"
        with lock:
            print(Style.BRIGHT + ts + color + f" [{tag}] " + Fore.RESET + content + Fore.RESET)

    @staticmethod
    def Ask(tag: str, content: str, color):
        ts = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"
        return input(Style.BRIGHT + ts + color + f" [{tag}] " + Fore.RESET + content + Fore.RESET)
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    clear_terminal()
    print(f""" 
{Fore.LIGHTBLUE_EX} ______   ______     ______     __    __     ______     ______     ______     __   __    
/\  == \ /\  == \   /\  __ \   /\ "-./  \   /\  __ \   /\  ___\   /\  ___\   /\ "-.\ \   
\ \  _-/ \ \  __<   \ \ \/\ \  \ \ \-./\ \  \ \ \/\ \  \ \ \__ \  \ \  __\   \ \ \-.  \  
 \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\ "\_\ 
  \/_/     \/_/ /_/   \/_____/   \/_/  \/_/   \/_____/   \/_____/   \/_____/   \/_/ \/_/ 
                        
""")
class O:
    def __init__(self, proxy) -> None:
        self.session = tls_client.Session(client_identifier="chrome112")
        self.proxy = proxy
        self.gen()

    def p(self, *args, **kwargs):
        while True:
            try:
                return self.session.post(*args, **kwargs)
            except Exception as e:
                # print_exc()
                continue

    def gen(self):
        global genned
        response = self.p('https://api.discord.gx.games/v1/direct-fulfillment', json={
            'partnerUserId': str(uuid.uuid4()),
        }, proxy=self.proxy)
        if response.status_code == 429:
            Logger.Sprint("Ratelimit", "You are being rate limited!", Fore.LIGHTYELLOW_EX)
            return
        ptoken = response.json()['token']
        link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{ptoken}"
        Logger.Sprint(f"Valid", "https://discord.com/promotions/hiddenlink", Fore.LIGHTGREEN_EX)
        genned += 1
        with lock:
            open("promos.txt", 'a').write(f"{link}\n")

def gnr():
    try:
        proxy = "http://" + choice(open("proxies.txt").read().splitlines())
    except:
        proxy = None
    while True:
        try:
            O(proxy)
        except:
            print_exc()

if __name__ == "__main__":
    init()
    welcome_message()
    t = int(Logger.Ask("+", "Put a number to generate between 100 | 1000 > ", Fore.LIGHTBLUE_EX))
    with ThreadPoolExecutor(max_workers=t + 1) as exc:
        for i in range(t):
            exc.submit(gnr)




#╔═════════════════════════════════════════════════════╗
#║    || - ||        Code By Jimo            || - ||   ║
#╚═════════════════════════════════════════════════════╝
          