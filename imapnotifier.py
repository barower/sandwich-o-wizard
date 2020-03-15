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
    server.select_folder('INBOX', readonly=True)
    subject = str(make_header(decode_header(str(server.fetch(uid, 'ENVELOPE')[uid][b'ENVELOPE'].subject))))
    subject = subject[2:-1].strip()
    server.close_folder()
    return subject

def get_unseen_uids(server):
    server.select_folder('INBOX', readonly=True)
    retval = server.search(criteria=[u'UNSEEN'])
    server.close_folder()
    return retval

def mail_move(server, uid, folder):
    server.select_folder('INBOX', readonly=False)
    server.copy(uid, folder)
    server.delete_messages(uid)
    server.close_folder()

if __name__ == "__main__":

    server = login()

    catering_folder = Folder(server, "Jedzenie")

    while True:
        print("Checking emails")
        for uid in get_unseen_uids(server):
            subject = get_subject(server, uid).lower()
            if subject in filtry:
                print(subject + " in filters, moving")
                mail_move(server, uid, catering_folder.folder)

        time.sleep(SLEEP_TIME)
        os.system("clear")

