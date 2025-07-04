import subprocess
import platform
import re
import os
import random
import time
from datetime import datetime
from colorama import Fore, Style, init
import pyfiglet
import psutil
import requests
import speedtest
from cryptography.fernet import Fernet
import wmi

# ========== Initialize Libraries ==========
init(autoreset=True)
c = wmi.WMI()

# ========== Quotes ==========
quotes = [
    "🔐 Security is not a product, but a process.",
    "💻 Code is like a ninja – fast, silent, and precise.",
    "🧠 Hack the planet, protect your data.",
    "🎯 Tools don't hack, people do.",
    "🕶️ Every byte matters in cyber space.",
    "🚀 First, solve the problem. Then, write the code.",
    "🧬 Simplicity is the ultimate sophistication.",
    "🔥 You don’t need eyes to see, you need vision.",
    "📡 Data is the new oil – protect it.",
    "💡 Innovation is born from necessity.",
    "🔍 Bugs are just undocumented features.",
    "⚙️ Keep calm and grep on.",
    "🔓 The best password is the one you can't remember.",
    "☠️ Hackers don’t break in – they walk through open doors.",
    "🔁 Rebooting is like sweeping your room under the rug.",
    "📊 Trust, but verify – even your system logs.",
    "🔄 There's no patch for human stupidity.",
    "🧩 Don't code harder, code smarter.",
    "🛡️ Encryption: Because privacy matters.",
    "👀 Real hackers wear hoodies and drink coffee.",
    "📁 Life is too short to manually sort files.",
    "💣 Delete system32 to boost FPS. (Just kidding!)",
    "🔧 If it works, don’t touch it.",
    "🌀 There’s always one more bug.",
    "⏱️ Compile time is thinking time.",
    "📌 Document your code or face your own wrath.",
    "🗂️ Backups are proof you once cared.",
    "📉 Downtime is not an option. Unless you're sleeping.",
    "🛠️ Coding: where hours of fun = minutes of running code.",
    "🧯 Try except finally: Try not to panic.",
    "👨‍💻 Eat, Sleep, Code, Repeat.",
    "📎 Your favorite function is now deprecated.",
    "🔋 Battery low... like your motivation.",
    "💻 A clean desk = a wiped hard drive.",
    "🧮 RAM is just a suggestion for Chrome.",
    "🚧 Under construction... like every good idea.",
    "🌐 DNS – the phonebook of the internet.",
    "🧠 AI can’t fix human error (yet).",
    "💾 Save early, save often.",
    "🐍 Python: Where whitespace is law.",
    "👾 Coding is debugging a bug you introduced while fixing a bug.",
    "📦 Install package, break system. Fix system, uninstall package.",
    "🛸 Tech support: Have you tried turning it off and on again?",
    "🔍 Who needs sleep when you have logs to tail?",
    "☕ Coffee > Sleep when code is compiling.",
    "🎲 50% of programming is Google. The other 50% is Stack Overflow.",
    "⚡ Your firewall is only as strong as your last update.",
    "🧟‍♂️ Zombie processes are real. Run `htop` and see.",
    "📡 Wi-Fi drops during online exams. Coincidence? I think not.",
    "🧙‍♂️ Code is poetry. Until it throws an exception."
]

# ========== Banner ==========
def animated_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = pyfiglet.figlet_format("NinjaBox")
    for char in banner:
        print(Fore.GREEN + char, end='', flush=True)
        time.sleep(0.0005)
    print(Fore.RED + "=" * 60)
    print(Fore.CYAN + f"📅 {datetime.now().strftime('%Y-%m-%d')}     🕒 {datetime.now().strftime('%H:%M:%S')}")
    print(Fore.YELLOW + random.choice(quotes))
    print(Fore.RED + "=" * 60 + "\n")

# ========== 1. View saved Wi-Fi passwords ==========
def wifi_passwords():
    print(Fore.CYAN + "\n[+] Saved Wi-Fi networks:")
    result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
    profiles = re.findall(r"All User Profile\s*: (.*)", result.stdout)
    for profile in profiles:
        profile = profile.strip()
        result2 = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
        password = re.search(r"Key Content\s*: (.*)", result2.stdout)
        print(Fore.YELLOW + f"📶 {profile} → 🔑 {password.group(1) if password else 'Unknown'}")

# ========== 2. System Information ==========
def system_info():
    print(Fore.CYAN + "\n[+] Full system information:")
    print(Fore.YELLOW + f"OS: {platform.system()} {platform.release()}")
    print(Fore.YELLOW + f"Platform: {platform.platform()}")
    print(Fore.YELLOW + f"CPU: {platform.processor()}")
    for cpu in c.Win32_Processor():
        print(Fore.YELLOW + f"CPU Name: {cpu.Name.strip()}")
        print(Fore.YELLOW + f"Cores: {cpu.NumberOfCores}")
        print(Fore.YELLOW + f"Threads: {cpu.NumberOfLogicalProcessors}")
    print(Fore.YELLOW + f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    try:
        for gpu in c.Win32_VideoController():
            print(Fore.YELLOW + f"GPU: {gpu.Name.strip()} ({gpu.DriverVersion})")
    except:
        print(Fore.YELLOW + f"GPU: Not detected")
    print(Fore.YELLOW + "\n[💽] Disk info:")
    for disk in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(disk.mountpoint)
            print(Fore.YELLOW + f"📁 {disk.device} → {round(usage.total / (1024**3), 2)} GB total, {round(usage.free / (1024**3), 2)} GB free")
        except:
            pass
    print(Fore.YELLOW + "\n[🛡️] Antivirus Info:")
    try:
        for av in c.Win32_Product():
            if "antivirus" in av.Name.lower():
                print(Fore.YELLOW + f"🔒 {av.Name}")
    except:
        print(Fore.YELLOW + "Antivirus not found or data unavailable")
    print(Fore.YELLOW + "\n[🌐] Network IP addresses:")
    addrs = psutil.net_if_addrs()
    for iface, infos in addrs.items():
        for info in infos:
            if info.family.name == 'AF_INET':
                print(Fore.YELLOW + f"🌐 {iface}: {info.address}")

# ========== 3. IP Info & Internet Speed ==========
def ip_info():
    print(Fore.CYAN + "\n[+] IP Address and Location:")
    try:
        res = requests.get("https://ipinfo.io/json").json()
        print(Fore.YELLOW + f"IP: {res.get('ip')}")
        print(Fore.YELLOW + f"City: {res.get('city')}, {res.get('region')}, {res.get('country')}")
        print(Fore.YELLOW + f"ISP: {res.get('org')}")
    except:
        print(Fore.RED + "[!] Failed to retrieve IP info")

def internet_speed():
    print(Fore.CYAN + "\n[+] Internet Speed:")
    st = speedtest.Speedtest()
    download = st.download() / 1024 / 1024
    upload = st.upload() / 1024 / 1024
    print(Fore.YELLOW + f"⬇️ Download: {download:.2f} Mbps")
    print(Fore.YELLOW + f"⬆️ Upload: {upload:.2f} Mbps")

# ========== 4. Joke & Motivation ==========
def show_joke():
    print(Fore.CYAN + "\n[😄] Random Joke:")
    print(Fore.YELLOW + random.choice(quotes))

def show_motivation():
    print(Fore.CYAN + "\n[🔥] Today's Motivation:")
    print(Fore.YELLOW + random.choice(quotes))

# ========== 5. File Encryption / Decryption ==========
def file_encryptor():
    print(Fore.CYAN + "\n[🔐] File Encryption")
    filename = input("Enter file name: ")
    if not os.path.exists(filename):
        print(Fore.RED + "[!] File not found!")
        return
    key = Fernet.generate_key()
    f = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()
    encrypted = f.encrypt(original)
    with open(filename + ".enc", 'wb') as enc_file:
        enc_file.write(encrypted)
    with open("key.key", 'wb') as key_file:
        key_file.write(key)
    print(Fore.GREEN + f"[+] {filename}.enc created. Key saved to key.key")

def file_decryptor():
    print(Fore.CYAN + "\n[🔓] File Decryption")
    enc_filename = input("Enter encrypted file name (.enc): ")
    if not os.path.exists(enc_filename):
        print(Fore.RED + "[!] File not found!")
        return
    if not os.path.exists("key.key"):
        print(Fore.RED + "[!] Key file (key.key) not found!")
        return
    with open("key.key", 'rb') as key_file:
        key = key_file.read()
    f = Fernet(key)
    with open(enc_filename, 'rb') as enc_file:
        encrypted = enc_file.read()
    try:
        decrypted = f.decrypt(encrypted)
        original_filename = enc_filename.replace(".enc", ".decrypted")
        with open(original_filename, 'wb') as dec_file:
            dec_file.write(decrypted)
        print(Fore.GREEN + f"[+] {original_filename} created.")
    except:
        print(Fore.RED + "[!] Error occurred during decryption!")

# ========== Menu ==========
def main():
    while True:
        animated_banner()
        print(Fore.CYAN + "1️⃣  View Wi-Fi Passwords")
        print("2️⃣  System Information")
        print("3️⃣  IP & Internet Speed")
        print("4️⃣  Random Joke")
        print("5️⃣  Motivation")
        print("6️⃣  Encrypt a File")
        print("7️⃣  Decrypt a File")
        print("8️⃣  Exit")
        choice = input(Fore.GREEN + "\nYour choice (1–8): ")

        if choice == '1':
            wifi_passwords()
        elif choice == '2':
            system_info()
        elif choice == '3':
            ip_info()
            internet_speed()
        elif choice == '4':
            show_joke()
        elif choice == '5':
            show_motivation()
        elif choice == '6':
            file_encryptor()
        elif choice == '7':
            file_decryptor()
        elif choice == '8':
            print(Fore.CYAN + "\n[👋] Thank you for using NinjaBox!")
            break
        else:
            print(Fore.RED + "[!] Invalid choice. Please enter between 1–8.")

        input(Fore.BLUE + "\n⏎ Press Enter to continue...")

if __name__ == "__main__":
    main()
