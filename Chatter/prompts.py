import re
from typing import List

from Bot import Message, Person

TEXT_MESSAGE_SIZE = 40
FORMAT = f"""(**don't use more that {TEXT_MESSAGE_SIZE} words don't use emoticons and don't wrap your answer with quotes and please don't repeat the same word to many times**)"""

def setup(alice:Person,bob:Person):
	return f"{alice.get_description()} and {bob.get_description()}. and they have been friends for a long time"

def chat_prompt(messages: List[Message]):
	chat_str = '\n'.join([f"{message.person.first_name}: {message.text}" for message in messages])
	return f"Can you please continue this chat(keep chat going and interesting ask many questions)\n```{chat_str}```"

def start_conversation_with_post(alice:Person,bob:Person,post):
	return f"Your task is to start conversation that includes original, unique, and relevant ideas that could help keep the conversation going, about a post titled `{post['title']}` it says `{post['excerpt']}`\n and most importantly {FORMAT}"


def senderStartChatReplyPrompt(message: Message):
	return f'''my friend sent me this message please write a reply in this format {FORMAT}!
	
{message.text}'''

def receiverStartChatReplyPrompt(message: Message):
	return f'''my friend sent me this text in a whatsapp chat please write a quick short reply

{message.text}'''

def senderInChatReplyPrompt(message: Message,backup_post):
	return f'''please reply to what my friend sent me try to keep the chat going about this topic try to come up with interesting facts about it or whatever you can to keep the conversation unique, interesting and original ask questions and explore new topics if want to and reply thoroughly to questions and use more than 40 word only if you're telling a story and most importantly stick to this format {FORMAT}

`{message.text}`'''


def receiverInChatReplyPrompt(message: Message,backup_post):
	return f'''please reply to what my friend sent reply with your experience as if you're not very familiar with the topic and don't ask questions and use a different writing style than {message.person.him()}
`{message.text}`'''

def endChatReplyPrompt(message: Message):
	return f'''please wrap up the chat. {FORMAT} {message.person.he()}  said

{message.text}'''

