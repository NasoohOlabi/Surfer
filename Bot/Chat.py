from dataclasses import dataclass, field
from typing import Dict, List, Literal, Optional

from .Message import Message
from .Person import Person
from Chatter.prompts import *


class Chat:
    messages: List[Message]
    correspondents: List[Person]

    def __init__(self, friend1: Person,friend2: Person,askGPT):
      self.correspondents = [friend1,friend2]
      self.askGPT = askGPT
      self.messages = []

    
    
    def reply_message(self)-> Optional[Message]:
      reply = self.askGPT(chat_prompt(self.messages))
      reply = ':'.join(reply.split(':')[1:])
      if len(reply.strip()) == 0:
        return None
      last_person = self.messages[-1].person
      replier = list(filter(lambda x : x.first_name != last_person.first_name,self.correspondents))[0]
      return Message(person=replier,text=reply)
    def chat_next(self):
      reply = self.reply_message()
      if reply is None:
        return False
      self.messages.append(reply)
      return True
    
    def next(self):
      if len(self.messages) == 0:
        raise Exception("Can't continue a nonexisting conversation!")
        # self.messages.append(Message(person=self.correspondents[0],text=self.askGPT(self.start_conversation_with_post(demo_post))))
      else:
        return self.chat_next()

    def render(self):
      lineHalfLen = 21
      print(f"{'-'*lineHalfLen} Chat {'-'*lineHalfLen}")
      for c in self.messages:
        print(c)
      print('-'*(lineHalfLen*2+6))
      
    def stream(self):
      for message in self.messages:
        yield message
      while self.next():
        yield self.messages[-1] 