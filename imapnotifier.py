from imapclient import  IMAPClient
from imapclient.exceptions import IMAPClientError
import time
import os
import sys

SLEEP_TIME = 1.5

class Folder():

    def __init__(self, server, foldername):
        self.server = server
        self.folder = foldername

        self.__create_folder()

    def __create_folder(self):
        try:
            self.server.select_folder(self.folder)
        except IMAPClientError:
            print("Cannot find folder {}, creating..".format(self.folder))
            self.server.create_folder(self.folder)

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

