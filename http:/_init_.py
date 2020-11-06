import random
import os

chittifile = open('chittidata.txt','r')
chittidata = chittifile.read()

chittifile_write = open('chittidata.txt','w')


my_bot = 'Chitti'

def startchat():
    print("Hi i am",my_bot)
    print("How can i help you")
    print("TYPE \n 1. To open something - 'open' \n 2. To save something 'save' \n 3. To open a file - 'open file'")
    order = input(">>>")
    if order == 'open':
        app_name = input("what? ")
        os.startfile(app_name)
        print("Done sir!")
        order = input(">>>")
    elif order == 'save':
        what_data = input("What: ")
        text = chittidata,'\n',what_data
        chittifile_write.writelines(text)
        print("Done Sir")
    elif order == 'open file':
        file_path = input("File path?: ")
        file = open(file_path,'r')
        file_user = file.read()
        print(file_user)
        print("Done Sir!")
    

    


startinput = input("What's your name? ")
if startinput != None:
    startchat()
