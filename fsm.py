from transitions.extensions import GraphMachine

from utils import send_text_message,send_image_message,play,game
import random as rand

class TocMachine(GraphMachine):
    ans = rand.randint(1,10)
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "play"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower()=="7"
#    def is_going_to_state1_1(self, event):
#        text = event.message.text
##        if game(int(text),self.ans)==1 or game(int(text),self.ans)==-1: text="continue"
##        elif game(int(text),self.ans)==-10:
##            text="fail"
##            self.chances=5
#        return text == "30"
    def is_going_to_state3(self, event):
        text = event.message.text
#        if game(int(text),self.ans)==0: text="win"
        return text == "100"
    def on_enter_state1(self, event):
        print("I'm entering state1")
#       self.ans = play()
        reply_token = event.reply_token
        out = "guess:"
        send_text_message(reply_token, out)
        

    def on_exit_state1(self):
        print("Leaving state1")
        self.go_back()
    def on_enter_state2(self, event):
        print("I'm entering state2")
        
        reply_token = event.reply_token
        send_text_message(reply_token, "win")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
    def on_enter_state3(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_text_message(reply_token, "win")
        #send_image_message(reply_token, "image")
#        self.chances=5
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")
