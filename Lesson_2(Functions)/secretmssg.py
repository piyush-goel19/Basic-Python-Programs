import os
import re
def rename_files():
    file_list = os.listdir(r"C:\Users\Piyush Goel\Downloads\secret message")
    print(file_list)
    spath = os.getcwd()
    print(spath)
    os.chdir(r"C:\Users\Piyush Goel\Downloads\secret message")
    for file in file_list:
        print("old file name - ",file)
        print("new file name - ",re.sub('[0-9]+','',file))
        os.rename(file,re.sub('\d+','',file))

    os.chdir(spath)    

rename_files()
