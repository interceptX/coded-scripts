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
            reply = "\n[-] zoom account not yet setup!"
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        def report_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                uid = words[1]
            else:
                print("[+] cant output second word!")
            report = f"\n[+] facebook uid: {uid}\n[+] auto report activated\n[+] sending malicious report\n[+] massive report lock"
            self.send(Message(text=report), thread_id=thread_id, thread_type=thread_type)

        def stop_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                name = words[1]
            else:
                print("[+] cant output second word!")
            stop = f"\n Yamete, Yamete Kudasai! {name}, Im so Horny!"
            self.send(Message(text=stop), thread_id=thread_id, thread_type=thread_type)

        def hotdog_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                name = words[1]
            else:
                print("[+] cant output second word!")
            hotdog = f" Would you like to eat my hotdogs Mr.{name}"
            self.send(Message(text=hotdog), thread_id=thread_id, thread_type=thread_type)

 
        def pizza_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                name = words[1]
            else:
                print("[+] cant output second word!")
            pizza = f" Mr.{name} love to eat pizza of a woman! Im glad he always made it."
            self.send(Message(text=pizza), thread_id=thread_id, thread_type=thread_type)

        def webapp_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                website = words[1]
            else:
                print("[+] cant output second word!")
            webapp = f"\n[+] getting subdomain: {website}\n"
            self.send(Message(text=webapp), thread_id=thread_id, thread_type=thread_type)
 
        def ipaddr_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                host = words[1]
            else:
                print("[+] cant output second word!")
            ipaddr = f"\n[+] getting ip address info\n[+] target: {host}"
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
                elif "report" in message.lower(): report_command(message.lower())
                elif "adel" in message.lower(): adel_info()
                elif "stop" in message.lower(): stop_command(message.lower())
                elif "hotdog" in message.lower(): hotdog_command(message.lower())
                elif "pizza" in message.lower(): pizza_command(message.lower())
                elif "webapp" in message.lower(): webapp_command(message.lower())
                elif "ipaddr" in message.lower(): ipaddr_command(message.lower())

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
