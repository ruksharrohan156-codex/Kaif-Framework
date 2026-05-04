import os
import time

# Colour Codes
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
B = '\033[1;34m' # Blue
P = '\033[1;35m' # Purple
C = '\033[1;36m' # Cyan
W = '\033[1;37m' # White

def banner():
    os.system('clear')
    print(f"""{C}
  ██╗  ██╗ █████╗ ██╗███████╗    {P}███████╗██╗  ██╗ █████╗ ██╗██╗  ██╗██╗  ██╗
  ██║ ██╔╝██╔══██╗██║██╔════╝    {P}██╔════╝██║  ██║██╔══██╗██║██║ ██╔╝██║  ██║
  █████╔╝ ███████║██║█████╗      {P}███████╗███████║███████║██║█████╔╝ ███████║
  ██╔═██╗ ██╔══██║██║██╔══╝      {P}╚════██║██╔══██║██╔══██║██║██╔═██╗ ██╔══██║
  ██║  ██╗██║  ██║██║██║         {P}███████║██║  ██║██║  ██║██║██║  ██╗██║  ██║
  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝         {P}╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
 {R}
  ██████╗ ███████╗███████╗██╗ ██████╗██╗ █████╗ ██╗
 ██╔═══██╗██╔════╝██╔════╝██║██╔════╝██║██╔══██╗██║
 ██║   ██║█████╗  █████╗  ██║██║     ██║███████║██║
 ██║   ██║██╔══╝  ██╔══╝  ██║██║     ██║██╔══██║██║
 ╚██████╔╝██║     ██║     ██║╚██████╗██║██║  ██║███████╗
  ╚═════╝ ╚═╝     ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝

    {G}╔══════════════════════════════════════════════════╗
    {G}║ {W}Developer: {C}Kaif Shaikh Official {G}║ {W}Version: {Y}12.1 {G}║
    {G}╚══════════════════════════════════════════════════╝
    """)

def main_menu():
    banner()
    print(f"{G}  [{W}01{G}] {C}Check My IP           {G}[{W}04{G}] {P}ZPhisher")
    print(f"{G}  [{W}02{G}] {Y}MaxPhisher            {G}[{W}05{G}] {B}Tool-X")
    print(f"{G}  [{W}03{G}] {P}PyPhisher             {G}[{W}00{G}] {R}Exit Framework")
    print(f"{G}--------------------------------------------------")

    choice = input(f"{C}Kaif-Official{W}@{C}Terminal{W}:~# {W}")

    if choice == '1' or choice == '01':
        print(f"\n{Y}[*] Fetching your IP...{W}")
        os.system("curl -s ifconfig.me && echo ''")
    elif choice == '2' or choice == '02':
        os.system("cd ~/MaxPhisher && python3 maxphisher.py")
    elif choice == '3' or choice == '03':
        os.system("cd ~/PyPhisher && python3 pyphisher.py")
    elif choice == '4' or choice == '04':
        os.system("cd ~/zphisher && bash zphisher.sh")
    elif choice == '5' or choice == '05':
        os.system("cd ~/Tool-X && python3 tool-x.py")
    elif choice == '0' or choice == '00':
        print(f"\n{R}Goodbye Kaif Shaikh Official!{W}")
        exit()
    else:
        print(f"\n{R}[!] Invalid Option!{W}")
        time.sleep(1)

    input(f"\n{G}[!] Press Enter to return...")
    main_menu()

if __name__ == "__main__":
    main_menu()
