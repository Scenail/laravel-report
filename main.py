from requests import get
from threading import Thread, Lock
from sys import argv
from datetime import datetime
from colorama import Fore, init
from random import randint
from socket import inet_ntoa
from struct import pack
from time import sleep
from os import _exit

init()

class colors():
    green = Fore.GREEN

class checker(object):
    def __init__(self):
        self.no = 0

    def check(self, lock, output_file):
        self.no += 1
        ip = f"http://{inet_ntoa(pack('>I', randint(1, 0xffffffff)))}/.env"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        }
        try:
            get_env = get(ip, headers=headers, timeout=20)
            print(f"{self.no} {ip}")
            with lock:
                with open(output_file, 'a') as file:
                    file.write(ip + '\n')
        except Exception as e:
            print(f"{self.no} Ip not found")

    def main(self, output_file="liveip.txt"):
        lock = Lock()
        while True:
            f1 = Thread(target=self.check, args=(lock, output_file), daemon=True)
            f1.start()
            sleep(0.001)
        f1.join()
        _exit(0)

if __name__ == "__main__":
    checker().main()
