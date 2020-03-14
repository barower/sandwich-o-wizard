from imapclient import  IMAPClient
from imapclient.exceptions import IMAPClientError

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

