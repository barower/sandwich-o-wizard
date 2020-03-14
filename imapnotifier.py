from imapclient import  IMAPClient
from folder import Folder
import email
from email.header import decode_header, make_header
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

    server.select_folder('INBOX', readonly=True)

    while True:
        print("Checking emails")
        for uid in server.search(criteria=[u'UNSEEN']):
            subject = (str(make_header(decode_header(str(server.fetch(uid, 'ENVELOPE')[uid][b'ENVELOPE'].subject)))).lower())
            print(subject)

        time.sleep(SLEEP_TIME)
        os.system("clear")

