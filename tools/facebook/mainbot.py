from fbchat import Client  
from fbchat.models import *
import sys
import random

class EchoBot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        def welcome_command():
            response = "Hey! I am MarvelBot Version 1.0\n\nFeel free to use 'help' command to know more."
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)

        def help_command(): 
            response = "\nMarvelBot v1.0 commands:\n\n- info  = bot information\n- zoom  = zoom link meeting\n- report = banning facebook target"
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)

        def info_command():
            response = "\nProg Language: Python 3.11\nBot name: MarvelBot\nVersion: 1.0\nLocation: Philippines\nStatus: Retard\nDeveloper: Marvel Gulane"
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)

        def zoom_command():
            response = "\nZoom account not yet setup!"
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)

        def report_command():
            response = "\nCommand: report <target_user_id>\n\nThis might result in banning a facebook user!"
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)

        def troll_command():
            txt  = "/home/interceptX/notes/tools/facebook/troll.txt"
            with open(txt,'r') as file:
                lines = file.readlines()
            random_line = random.choice(lines)
            self.send(Message(text=random_line), thread_id=thread_id, thread_type=thread_type)

        try:
            if author_id != self.uid: 
                message = message_object.text.lower()
                if "hi" in message: welcome_command()
                elif "help" in message: help_command()
                elif "info" in message: info_command()
                elif "zoom" in message: zoom_command()
                elif "troll" in message: troll_command()
                elif "report" in message: report_command()

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
