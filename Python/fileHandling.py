import os

FILE_PATH = "sample.txt"

class File:
    def create_file():
        """create a file if not exists"""
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH , "w"):
                pass


newFile = File.create_file()  

