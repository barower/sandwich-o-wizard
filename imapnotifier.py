from imapclient import  IMAPClient
from folder import Folder
import time
import os
import sys

SLEEP_TIME = 1.5

def login():
    with open("passes") as f:
        text = f.read().split()
        url = text[0]
        login = text[1]
        password = text[2]
        server = IMAPClient(url, use_uid=True)
        server.login(login, password)
        return server

if __name__ == "__main__":

    server = login()

    jedzenie = Folder(server, "Jedzenie")

    while True:
        print("Checking emails")

        time.sleep(SLEEP_TIME)
        os.system("clear")

