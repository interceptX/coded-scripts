from fbchat import Client  
from fbchat.models import *
import subprocess
import sys
import random

class EchoBot(Client):

    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=None, **kwargs):
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
            print('[+] user used welcome command.')

        def help_command(): 
            txt  = "/home/interceptX/notes/tools/facebook/data/help.txt"
            with open(txt,'r') as file:
                lines = file.read()
            reply = lines
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used help command.')

        def adel_info(): 
            txt  = "/home/interceptX/notes/tools/facebook/data/adel.txt"
            with open(txt,'r') as file:
                lines = file.read()
            reply = lines
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used adel info.')


        def info_command():
            txt = "/home/interceptX/notes/tools/facebook/data/info.txt"
            with open(txt, 'r') as file:
                lines = file.read()
            reply = lines
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used bot info command.')

        def zoom_command():
            reply = "\n[-] zoom account not yet setup!"
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used zoom command.')

        def report_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                uid = words[1]
            else:
                print("[+] cant output second word!")
            report = f"\n[+] facebook uid: {uid}\n[+] auto report activated\n[+] sending malicious report\n[+] massive report lock"
            self.send(Message(text=report), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used report command.')

        def stop_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                name = words[1]
            else:
                print("[+] cant output second word!")
            stop = f"\n Yamete, Yamete Kudasai! {name}, Im so Horny!"
            self.send(Message(text=stop), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used stop command.')

        def hotdog_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                name = words[1]
            else:
                print("[+] cant output second word!")
            hotdog = f" Would you like to eat my hotdogs Mr.{name}"
            self.send(Message(text=hotdog), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used a hotdog command.')
 
        def pizza_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                name = words[1]
            else:
                print("[+] cant output second word!")
            pizza = f" Mr.{name} love to eat pizza of a woman! Im glad he always made it."
            self.send(Message(text=pizza), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used pizza command.')

        def webapp_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                website = words[1]
            else:
                print("[+] cant output second word!")
            target = website
            filetext = '/home/interceptX/notes/tools/facebook/data/subdomains.txt'
            webapp = f"\n[+] getting subdomain: {target}\n[+] subdomain lists\n"
            command = f"curl -s 'https://crt.sh/?q=%25.{target}&output=json' | jq -r '.[].name_value' | sort -u "
            data = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = data.communicate()
            if output:
                with open(filetext, 'w') as file:
                    file.write(output.decode())
                    file.close()
                with open(filetext, 'r') as file:
                    data = file.read()
                goodresponse = webapp + data
                self.send(Message(text=goodresponse), thread_id=thread_id, thread_type=thread_type)
            if error:
                with open(filetext, 'w') as file:
                    file.write(error.decode())
                    file.close()
                with open(filetext, 'r') as file:
                    data = file.read()
                badresponse = webapp + data
                self.send(Message(text=badresponse), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used a webapp command.') 


        def ipaddr_command(sentence):
            words = sentence.split()
            if len(words) >= 2:
                host = words[1]
            else:
                print("[+] cant output second word!")
            ipaddr = f"\n[+] getting ip address info\n[+] target: {host}\n[+] server response:\n"
            filetext = '/home/interceptX/notes/tools/facebook/data/ipinfo.txt'
            command = f"curl -s ipinfo.io/{host} | jq '.hostname, .city, .region, .country, .loc, .org, .postal, .timezone'"
            data = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = data.communicate()
            if output:
                with open(filetext, 'w') as file:
                    file.write(output.decode())
                    file.close()
                with open(filetext, 'r') as file:
                    data = file.read()
                goodresponse = ipaddr + data
                self.send(Message(text=goodresponse), thread_id=thread_id, thread_type=thread_type)
            if error:
                with open(filetext, 'w') as file:
                    file.write(error.decode())
                    file.close()
                with open(filetext, 'r') as file:
                    data = file.read()
                badresponse = ipaddr + data
                self.send(Message(text=badresponse), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used a ipaddr command.')

        def troll_command():
            txt  = "/home/interceptX/notes/tools/facebook/data/troll.txt"
            with open(txt,'r') as file:
                lines = file.readlines()
            random_line = random.choice(lines)
            self.send(Message(text=random_line), thread_id=thread_id, thread_type=thread_type)
            print('[+] user used a troll command')

        def chat_command():
            txt  = "/home/interceptX/notes/tools/facebook/data/random.txt"
            with open(txt,'r') as file:
                lines = file.readlines()
            random_chat = random.choice(lines)
            self.send(Message(text=random_chat), thread_id=thread_id, thread_type=thread_type)
            print('[+] bot currently participating conversation.')


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
                elif "a" or "e" in message.lower(): chat_command()


        except KeyboardInterrupt:
            print("[+] facebook bot terminated!")
            sys.exit(0)

session_cookies = {
}

try:
    client = EchoBot("", "", session_cookies=session_cookies)
    if client.isLoggedIn() is True:
        print("[+] facebook bot successfully logged in!")
        print("[+] facebook bot client will now listen conversations.")
        if client.listen() is True:
            print("[+] facebook bot client is actively listening conversations.")
        else:
            print("[-] facebook bot listening something went wrong!.")
    else:
        print("[-] something went wrong about the bot!")

except FBchatUserError:
    print("[+] facebook bot terminated!")
    sys.exit(0)
