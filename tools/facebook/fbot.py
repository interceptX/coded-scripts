#LOAD IN THE LIBRARIES
from fbchat import Client
from fbchat.models import *


#CLASS FOR THE BOT
class MessBot(Client):

  #Read Messages, See Messages from other users
  def onMessage(self,
                mid=None,
                author_id=None,
                message_object=None,
                thread_id=None,
                thread_type=ThreadType.USER,
                **kwargs):
    try:
      msg = str(message_object).split(",")[15][14:-1]
      print(msg)
      #If user sent video or else user sent text
      if ("//video.xx.fbcdn" in msg):
        msg = msg
      else:
        msg = str(message_object).split(",")[19][20:-1]
    except:
      try:
        msg = (message_object.text).lower()
        print(msg)
      except:
        pass


#Reply to the user/send message

    def sendMsg():
      if (author_id != self.uid):
        self.send(Message(text=reply),
                  thread_id=thread_id,
                  thread_type=thread_type)

  #MESSAGE SENDING

    if (author_id != self.uid):
      if ("Hi" in msg):
        reply = "I am mikibot v1.0 created by Marvel Gulane under python language type {help} command"
        sendMsg()
      elif ("help" in msg):
        reply = """
                    - hi - info bot message
                    - help - command information bot
                    - hack - please specify target! - help <domain_target>
                """
        sendMsg()
    else:
      pass

#Get Cookies Using GET TOKEN COOKIES (https://chrome.google.com/webstore/detail/get-token-cookie/naciaagbkifhpnoodlkhbejjldaiffcm)
session_cookies = {
  #"sb": "",
  #"fr": "",
  #"c_user": "",
  #"datr": "",
  #"xs": "",

    "sb":"c4tcZlFtlA4fFhcvmshz9coN",
    "datr":"c4tcZshLptqdSpiD1e68rNNE",
    "c_user":"61558478504573", 
    "xs":"7%3A15TI_G5BUifdxA%3A2%3A1717341058%3A-1%3A7470",
    "fr":"0dRs9pDE5abXtiFMb.AWXwVPh8h2f6Ch6_HOvlZVC3t9Q.BmXIuC..AAA.0.0.BmXIuF.AWXH__I2h3U",
    "wd":"901x285", 
    "presence":"C%7B%22lm3%22%3A%22u.61558478504573%22%2C%22t3%22%3A%5B%7B%22o%22%3A0%2C%22i%22%3A%22u.61558478504573%22%7D%5D%2C%22utc3%22%3A1717341127218%2C%22v%22%3A1%7D"

}

bot = MessBot('', '', session_cookies=session_cookies)
print(bot.isLoggedIn())

try:
  bot.listen()
except:
  bot.listen()
