from imapclient import  IMAPClient
from imapclient.exceptions import IMAPClientError
import time
import os

SLEEP_TIME = 1.5

class Folder():

    def __init__(self, server, foldername, soundpath, recipients=None):
        self.server = server
        self.folder = foldername
        self.sound = soundpath
        self.recipients = recipients

        self.__create_folder()

        self.msgcount = self.get_msg_count()

    def __create_folder(self):
        try:
            self.server.select_folder(self.folder)
        except IMAPClientError:
            print("Cannot find folder {}, creating..".format(self.folder))
            self.server.create_folder(self.folder)

    def get_msg_count(self):
        select_info = self.server.select_folder(self.folder)

        if self.recipients is None:
            return select_info[b'EXISTS']
        else:
            return len(self.server.search(['TO', self.recipients]))


if __name__ == "__main__":
    server = IMAPClient('PLACEHOLDER', use_uid=True)
    server.login('PLACEHOLDER', 'PLACEHOLDER')

    #recipientaddress = 'dzialkowa@enigma.com.pl'
    recipientaddress = None

    Kanapki = Folder(server, "Kanapki", "")
    Catering50 = Folder(server, "Catering50", "")
    Slimak = Folder(server, "Slimak", "")
    Sushi = Folder(server, "Sushi", "")

    folders = [Kanapki, Catering50, Slimak, Sushi]

    while True:
        for folder in folders:
            count = folder.get_msg_count()
            print('{} messages in folder {}'.format(count, folder.folder))

        time.sleep(SLEEP_TIME)
        os.system("clear")

