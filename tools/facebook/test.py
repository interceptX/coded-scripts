from fbchat import Client
from fbchat.models import *
from chatbot import demo

class EchoBot(Client):

    def onmessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

    def sendmsg():
        if (author_id != self.uid):
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

    if ( author_id != self.uid ):
        message = message_object.text
        if ("test" in message): reply="ni hao!";sendmsg()
session_cookies = {
    "sb":"c4tcZlFtlA4fFhcvmshz9coN",                                                                                                   
    "datr":"c4tcZshLptqdSpiD1e68rNNE",                                                                                                                                                                                        
    "c_user":"61558478504573",                                                                                                                                                                                                
    "xs":"7%3A15TI_G5BUifdxA%3A2%3A1717341058%3A-1%3A7470",                                                                                                                                                                  
    "fr":"0dRs9pDE5abXtiFMb.AWXwVPh8h2f6Ch6_HOvlZVC3t9Q.BmXIuC..AAA.0.0.BmXIuF.AWXH__I2h3U",                                                                                                                                  
    "wd":"901x285",                                      
    "presence":"C%7B%22lm3%22%3A%22u.61558478504573%22%2C%22t3%22%3A%5B%7B%22o%22%3A0%2C%22i%22%3A%22u.61558478504573%22%7D%5D%2C%22utc3%22%3A1717341127218%2C%22v%22%3A1%7D"
 
}

client = EchoBot("","",session_cookies=session_cookies)
client.listen()
