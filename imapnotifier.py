from imapclient import  IMAPClient
from folder import Folder
from mailfilter import Mailfilter
import email
from email.header import decode_header, make_header
import time
import os
import sys
from getpass import getpass
import logging

SLEEP_TIME = 1.5

def login():
    with open("passes") as f:
        text = f.read().split()
        url = text[0]
        login = text[1]
        password = getpass("Password to {}@{}: ".format(url, login))
        server = IMAPClient(url, use_uid=True)
        server.login(login, password)
        return server

def get_subject(server, uid):
    server.select_folder('INBOX', readonly=True)
    subject = str(make_header(decode_header(str(server.fetch(uid, 'ENVELOPE')[uid][b'ENVELOPE'].subject))))
    subject = subject[2:-1].strip()
    server.close_folder()
    return subject

def get_uids(server, search_criteria):
    server.select_folder('INBOX', readonly=True)
    retval = server.search(criteria=search_criteria)
    server.close_folder()
    return retval

def mail_move(server, uid, folder):
    server.select_folder('INBOX', readonly=False)
    server.copy(uid, folder)
    server.delete_messages(uid)
    server.close_folder()

if __name__ == "__main__":

    filt = Mailfilter()

    filt.add_filter("kanapki", "~/Sounds/playsound.sh kanapki")
    filt.add_filter("slimak", "~/Sounds/playsound.sh slimak")
    filt.add_filter("ślimak", "~/Sounds/playsound.sh slimak")
    filt.add_filter("sushi", "~/Sounds/playsound.sh sushi")
    filt.add_filter("catering", "~/Sounds/playsound.sh catering50")

    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='imapfilter.log', level=logging.INFO)

    server = login()

    catering_folder = Folder(server, "Jedzenie")

    with open("search_criteria", "r") as f:
        search_criteria = f.read().split()

    while True:
        logging.debug("Checking emails")

        try:
            for uid in get_uids(server, search_criteria):
                subject = get_subject(server, uid).lower()
                if filt.do_filter(subject):
                    logging.info(subject + " in filters, moving")
                    mail_move(server, uid, catering_folder.folder)
        except Exception as ex:
            logging.error("{}".format(ex))


        filt.run_pending_scripts()
        time.sleep(SLEEP_TIME)
        os.system("clear")

