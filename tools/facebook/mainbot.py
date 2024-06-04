from fbchat import Client  
from fbchat.models import *
import sys
import random

class EchoBot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        def sendmsg():
            if (author_id != self.uid):
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)


        def welcome_command():
            txt  = "/home/interceptX/notes/tools/facebook/data/banner.txt"
            with open(txt,'r') as file:
                lines = file.read()
            reply = lines
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        def help_command(): 
            txt  = "/home/interceptX/notes/tools/facebook/data/help.txt"
            with open(txt,'r') as file:
                lines = file.read()
            reply = lines
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        def adel_info(): 
            txt  = "/home/interceptX/notes/tools/facebook/data/adel.txt"
            with open(txt,'r') as file:
                lines = file.read()
            reply = lines
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)


        def info_command():
            txt = "/home/interceptX/notes/tools/facebook/data/info.txt"
            with open(txt, 'r') as file:
                lines = file.read()
            reply = lines
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        def zoom_command():
            reply = "\nzoom account not yet setup!"
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        def report_command():
            reply = "\nCommand: report {target_id}\nNote: This might result banning facebook user."
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        def troll_command():
            txt  = "/home/interceptX/notes/tools/facebook/data/troll.txt"
            with open(txt,'r') as file:
                lines = file.readlines()
            random_line = random.choice(lines)
            self.send(Message(text=random_line), thread_id=thread_id, thread_type=thread_type)

        try:
            if author_id != self.uid:
                message = message_object.text
                if "hi" in message.lower(): welcome_command()
                elif "help" in message.lower(): help_command()
                elif "info" in message.lower(): info_command()
                elif "zoom" in message.lower(): zoom_command()
                elif "troll" in message.lower(): troll_command()
                elif "report" in message.lower(): report_command()
                elif "adel" in message.lower(): adel_info()
        except KeyboardInterrupt:
            print("[+] facebook bot terminated!")
            sys.exit(0)
                
session_cookies = {
 
}

client = EchoBot("", "", session_cookies=session_cookies)
if client.isLoggedIn() is True:
    print("[+] facebook bot successfully logged in!")
else:
    print("[-] something went wrong about the bot!")

try:
    print(client.listen())
except KeyboardInterrupt:
    print("[+] facebook bot terminated!")
    sys.exit(0)
