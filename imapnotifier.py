from imapclient import  IMAPClient
from folder import Folder
import email
from email.header import decode_header, make_header
import time
import os
import sys

SLEEP_TIME = 1.5

filtry = 'kanapki ślimak slimak catering sushi'

def login():
    with open("passes") as f:
        text = f.read().split()
        url = text[0]
        login = text[1]
        password = text[2]
        server = IMAPClient(url, use_uid=True)
        server.login(login, password)
        return server

def get_subject(server, uid):
    subject = str(make_header(decode_header(str(server.fetch(uid, 'ENVELOPE')[uid][b'ENVELOPE'].subject))))
    subject = subject[2:-1].strip()
    return subject

if __name__ == "__main__":

    server = login()

    jedzenie = Folder(server, "Jedzenie")

    server.select_folder('INBOX', readonly=True)

    while True:
        print("Checking emails")
        for uid in server.search(criteria=[u'UNSEEN']):
            subject = get_subject(server, uid).lower()
            if subject in filtry:
                print(subject + " is in filter list")

        time.sleep(SLEEP_TIME)
        os.system("clear")

