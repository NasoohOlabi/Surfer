import re
from turtle import back
from typing import Dict, List, Optional

from h11 import SEND_RESPONSE

from Bot import Message, Person

TEXT_MESSAGE_SIZE = 40
SENDER_FORMAT = f"""and most importantly stick to the following format: don't use more that {TEXT_MESSAGE_SIZE} words don't use emoticons and don't wrap your answer with quotes and please don't repeat the same word too many times."""
RECEIVER_FORMAT = f"""and most importantly stick to this format don't ask questions and don't wrap your answer with quotes and use a different writing style than hers."""

def setup(alice:Person,bob:Person):
	return f"{alice.get_description()} and {bob.get_description()}. and they have been friends for a long time"

def chat_prompt(messages: List[Message]):
	chat_str = '\n'.join([f"{message.person.first_name}: {message.text}" for message in messages])
	return f"Can you please continue this chat(keep chat going and interesting ask many questions)\n```{chat_str}```"

def start_conversation_with_post(alice:Person,bob:Person,post):
	return f"Your task is to start conversation that includes original, unique, and relevant ideas that could help keep the conversation going, about a post titled `{post['title']}` it says `{post['excerpt']}`\n {SENDER_FORMAT}"


def senderStartChatReplyPrompt(message: Message):
	return f'''my friend sent me this message {SENDER_FORMAT}
	
{message.text}'''

def receiverStartChatReplyPrompt(message: Message):
	return f'''my friend sent me this text in a whatsapp chat please write a quick short reply

{message.text}'''

def senderInChatReplyPrompt(message: Message,backup_post:Optional[Dict[str,str]]=None):
	bp = f'IF IT\'S NECESSARY CHANGE THE TOPIC TO THIS POST \ntitle:\n```{backup_post["title"]}```\ncontent:```{backup_post["excerpt"]}```' if backup_post is not None else ''
	return f'''please reply to what my friend sent me try to keep the chat going about this topic try to come up with interesting facts about it or whatever you can to keep the conversation unique, interesting and original. ask questions about opinions and experiences and explore similar topics to and reply thoroughly to your own questions after you hear {message.person.his()} answers  and use more than 40 word only if you're telling a story {SENDER_FORMAT} {bp}

`{message.text}`'''


def receiverInChatReplyPrompt(message: Message):
	return f'''please reply to what my friend sent reply with your experience and unique opinions about the topic {RECEIVER_FORMAT}
`{message.text}`'''

def endChatReplyPrompt(message: Message):
	return f'''please wrap up the chat. {SENDER_FORMAT} {message.person.he()}  said

{message.text}'''

