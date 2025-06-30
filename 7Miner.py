import os
import subprocess
import sys
import requests
import random
import string
import time
import atexit
from colorama import Fore, init
from datetime import datetime
import keyboard

# ------------------- Check and install Python and libs -------------------

def is_python_installed():
    try:
        subprocess.check_output(["python", "--version"])
        return True
    except subprocess.CalledProcessError:
        return False

def install_python():
    print("Python is not installed. Download it from: https://www.python.org/downloads/")
    print("After installation, restart the program.")
    sys.exit()

def install_libraries():
    required_libraries = ["requests", "colorama", "keyboard"]
    for lib in required_libraries:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "show", lib], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Library '{lib}' is already installed.")
        except subprocess.CalledProcessError:
            print(f"Library '{lib}' not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print(f"Library '{lib}' installed successfully.")

# ------------------- ASCII -------------------

ascii_logo = """
 ███████╗ ███╗   ███╗██╗███╗   ██╗███████╗█████╗ 
 ╚════██║ ████╗ ████║██║████╗  ██║██╔════╝██╔═██╗       
     ██╔╝ ██╔████╔██║██║██╔██╗ ██║█████╗  █████╔╝            
    ██╔╝  ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔═██╗            
    ██║   ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║ ╚██╗
    ╚═╝   ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
"""

PickageAscii = """
           ██████████                   
         ██          ██████             █     █ ██  ██  ██  █
           ████████      ██             █  █  █ █ █ █ █ █ █ █
                  ███    ██             █ █ █ █ ███ ██  █  ██
                 ██  ██    ██           ██   ██ █ █ █ █ █   █
               ██  ██ ██   ██          
             ██  ██   ██   ██           "If you want to stop
           ██  ██     ██   ██            searching, press the
         ██  ██       ██   ██            ESC" key!!"
       ██  ██           ███   
     ██  ██                   
   ██  ██                    
   ████                      
"""

            
GoodbyeASCII = """            

                              █████████                                       ███   ███                                       ██                      
                            ████████████                                      ███   ███                                      ███                      
                           ████                ███           ███          ███ ███   ███  ███                     ████        ███                      
                          ████              ██████████   ██████████    ██████████   ███████████  ███     ███   █████████     ██                       
                          ███    ███████   ███     ███   ███     ███   ███    ███   ████    ████  ███   ████  ███    ███     ██                       
                          ███    ███████  ████     ████ ███      ████ ███     ███   ███      ███  ████  ███  ████████████    ██                       
                          ████       ███  ███      ████ ███      ████ ███     ███   ███      ███   ███ ███   ███             ██                       
                           ████      ███   ███     ███  ████     ███  ████    ███   ████    ████    █████     ███                                    
                             ███████████    █████████    ██████████    ██████████   ███████████      ████     ██████████     ███                      
                                █████         ████          ████         ████  ██   ██   ███         ███         █████       ██                       
                                                                                                    ███                                               
                                                                                                   ████                                               

"""    


# ------------------- Starting+CLS -------------------

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

# ------------------- Inputs -------------------

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().upper()
        if response in ['Y', 'N']:
            return response
        print(f"{Fore.RED}Invalid input. Please enter 'Y' or 'N'.")

def get_int_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                return value
            print(f"{Fore.RED}Input must be between {min_value} and {max_value}.")
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a valid number.")

def get_choice_input(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice.isdigit() and int(choice) in valid_choices:
            return int(choice)
        print(f"{Fore.RED}Invalid input. Valid options: {', '.join(map(str, valid_choices))}")

# ------------------- Files and cache -------------------

required_dirs = ["debug", "claimed"]
required_files = ["names.txt", "proxies.txt", "debug/cache.txt", "webhook.txt"]

for dir_path in required_dirs:
    os.makedirs(dir_path, exist_ok=True)

for file_path in required_files:
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            pass

with open("webhook.txt", "r") as f:
    webhook_url = f.read().strip()

cache_file = "debug/cache.txt"
current_proxy = None

def is_cached(username):
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            return username in [line.strip() for line in f]
    return False

def add_to_cache(username):
    with open(cache_file, "a") as f:
        f.write(f"{username}\n")

def clear_cache():
    if os.path.exists(cache_file):
        try:
            os.remove(cache_file)
            print(f"{Fore.CYAN}Cache cleared.")
        except PermissionError:
            print(f"{Fore.RED}Could not delete cache file. It may be in use.")

atexit.register(clear_cache)

# ------------------- Proxy -------------------

def load_proxies():
    global use_proxies, proxies
    if not use_proxies:
        proxies = [None]
        return

    proxy_path = "proxies.txt"
    if not os.path.exists(proxy_path):
        print(f"{Fore.RED}'proxies.txt' not found.")
        proxies = [None]
        return

    with open(proxy_path, "r") as f:
        lines = list(set(l.strip() for l in f if l.strip()))

    proxies = [{"http": f"http://{p}", "https": f"http://{p}"} for p in lines]
    print(f"{Fore.CYAN}Loaded {len(proxies)} proxies.")

    working = []
    for i, proxy in enumerate(proxies, 1):
        print(f"{Fore.LIGHTMAGENTA_EX}Testing proxies... ({i}/{len(proxies)})", end="\r")
        try:
            requests.get("https://api.mojang.com/", proxies=proxy, timeout=5)
            working.append(proxy)
        except:
            continue

    proxies[:] = working if working else [None]
    if working:
        print(f"{Fore.GREEN}Working proxies: {len(proxies)}")
    else:
        print(f"{Fore.RED}No working proxies found. Using direct connection.")
        use_proxies = False

proxy_index = 0
def get_next_proxy():
    global proxy_index
    proxy_index = (proxy_index + 1) % len(proxies)
    proxy = proxies[proxy_index]
    if proxy:
        print(f"{Fore.LIGHTMAGENTA_EX}Choosing a proxy...")
        print(f"{Fore.MAGENTA}Using proxy: '{proxy['http']}'")
    return proxy

# ------------------- Check -------------------

def check_minecraft_username(name):
    global base_wait_time, errors_429_consecutive, current_proxy
    url = f"https://api.mojang.com/users/profiles/minecraft/{name}"
    for attempt in range(3):
        try:
            if use_proxies and current_proxy is None:
                current_proxy = get_next_proxy()
            response = requests.get(url, timeout=10, proxies=current_proxy)

            if response.status_code == 200:
                return (False, f"{Fore.RED}Username '{name}' is UNAVAILABLE.")
            elif response.status_code == 404:
                return (True, f"{Fore.GREEN}Username '{name}' is AVAILABLE!")
            elif response.status_code == 429:
                current_proxy = get_next_proxy()
                return (None, "ERROR_429")
            else:
                return (False, f"{Fore.RED}Unexpected error: {response.status_code}")
        except requests.RequestException:
            current_proxy = get_next_proxy()
            time.sleep(1)
    return (False, f"{Fore.RED}Failed to check '{name}' after 3 attempts.")

# ------------------- Main -------------------

def main():
    print(ascii_logo)

    global use_proxies, proxies, base_wait_time, max_wait_time, min_wait_time, acceleration, deceleration, errors_429_consecutive, current_proxy
    base_wait_time, max_wait_time, min_wait_time = 1.0, 15.0, 0.2
    acceleration, deceleration = 0.9, 1.5
    errors_429_consecutive = 0
    current_proxy = None

    use_proxies = get_yes_no_input("- Use proxies? (Y/N): ") == "Y"
    load_proxies()

    use_name_list = get_yes_no_input("- Use names from 'names.txt'? (Y/N): ") == "Y"
    usernames_to_check = []

    if use_name_list:
        with open("names.txt", "r") as f:
            usernames_to_check = [line.strip() for line in f if line.strip()]
        if not usernames_to_check:
            print(f"{Fore.RED}No names found in file. Switching to random mode.")
            use_name_list = False

    if not use_name_list:
        length = get_int_input("- Username length (3 to 16): ", 3, 16)
        print("- Character type:\n  1. Letters\n  2. Numbers\n  3. Letters + Numbers\n  4. Letters + Numbers + _")
        choice = get_choice_input("- Choose a search type [1-4]: ", [1, 2, 3, 4])
        characters = {
            1: string.ascii_letters,
            2: string.digits,
            3: string.ascii_letters + string.digits,
            4: string.ascii_letters + string.digits + "_"
        }[choice]
        quantity = get_int_input("- How many usernames to check?: ", 1)
        def generate_username():
            while True:
                u = ''.join(random.choice(characters) for _ in range(length))
                if 3 <= len(u) <= 16 and not u.startswith("_") and not u.endswith("_"):
                    return u
        usernames_to_check = [generate_username() for _ in range(quantity)]

    os.system('cls' if os.name == 'nt' else 'clear')
    print(PickageAscii)
    print("\nChecking usernames...\n")
    available_count = 0
    log_filename = f"claimed/names_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    for i, username in enumerate(usernames_to_check, 1):
        if keyboard.is_pressed('esc'):
            print(f"{Fore.CYAN}Search aborted by user.")
            break
        if is_cached(username):
            print(f"{Fore.YELLOW}Username '{username}' already checked. Skipping... ({i}/{len(usernames_to_check)})")
            continue
        while True:
            available, result = check_minecraft_username(username)
            if result == "ERROR_429":
                print(f"{Fore.YELLOW}Waiting {base_wait_time:.1f}s before retrying...")
                time.sleep(base_wait_time)
            else:
                print(f"{result} ({i}/{len(usernames_to_check)})")
                if available:
                    available_count += 1
                    with open(log_filename, "a") as file:
                        file.write(username + "\n")
                    if webhook_url:
                        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        embed = {
                            "username": "7Miner Bot",
                            "embeds": [{
                                "title": "🎉 Available name found!",
                                "color": 0x00ff00,
                                "fields": [
                                    {"name": "👤 Name:", "value": f"[`{username}`](https://namemc.com/profile/{username})"},
                                    {"name": "📅 Found on:", "value": f"`{now}`"}
                                ]
                            }]
                        }
                        try:
                            requests.post(webhook_url, json=embed)
                        except: pass
                if available is not None:
                    add_to_cache(username)
                break

    if available_count == 0:
        print(f"\n{Fore.GREEN}- Check completed successfully!")
        print(f"{Fore.RED}- {available_count} Usernames available...")
    else:
        if webhook_url:
            print(f"\n{Fore.GREEN}- Check completed successfully!")
            print(f"{Fore.GREEN}- {available_count} Usernames available!")
            print(f"{Fore.GREEN}- Saved in '{log_filename}' and in your Webhook.")
        else:
            print(f"\n{Fore.GREEN}- Check completed successfully!")
            print(f"{Fore.GREEN}- {available_count} Usernames available!")
            print(f"{Fore.GREEN}- Saved in '{log_filename}'")

# ------------------- Main Loop -------------------

while True:
    main()
    again = get_yes_no_input("\nCheck more usernames? (Y/N): ")
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("webhook.txt", "r") as f:
        webhook_url = f.read().strip()
    if again != "Y":
        print(GoodbyeASCII)
        print(f"{Fore.CYAN}Exiting 7Miner. Bye!")
        time.sleep(1.5)
        break
