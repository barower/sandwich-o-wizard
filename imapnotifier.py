from imapclient import  IMAPClient
import time
import os

class Folder():

    def __init__(self, server, foldername, soundpath, recipients=None):
        self.server = server
        self.folder = foldername
        self.sound = soundpath
        self.recipients = recipients
        self.msgcount = self.get_msg_count()

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

        time.sleep(1.5)
        os.system("clear")

