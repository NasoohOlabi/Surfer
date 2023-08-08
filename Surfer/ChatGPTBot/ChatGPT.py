import time
from typing import Tuple

import selenium.webdriver as webdriver
# from Feed import Feed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..ScriptRunner import ScriptRunner
from .ChatGPTWebsite import ChatGPTWebsite


class ChatGPT:
	def __init__(self, driver:webdriver.Chrome,window:ChatGPTWebsite, name:str|None = None):
		self.driver = driver
		self.run_script = ScriptRunner(driver,'./Surfer/scripts/')
		self.name = name
		self.window = window

	def ask(self,prompt:str, newChat:bool = False) -> Tuple[str, 'ChatGPT']:
		self.window.focus()
		if newChat:
			self.run_script('chat.openai.new chat')()
			WebDriverWait(self.driver, 30).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, 'svg > circle+line+line+line+line+line+line+line+line'))# examples sun in new chat
			)
		else:
			if self.name:
				self.run_script('chat.openai.switch to chat name')(self.name)
				time.sleep(4)
		textarea = self.driver.find_element(By.CSS_SELECTOR,'textarea')

		JS_ADD_TEXT_TO_INPUT = """
			var elm = document.querySelector('textarea'), txt = arguments[0];
			elm.value += txt;
			elm.dispatchEvent(new Event('change'));
			"""
		prompts = prompt.split('\n')
		for line in prompts:
			self.driver.execute_script(JS_ADD_TEXT_TO_INPUT, line)
			textarea.send_keys(Keys.SHIFT + Keys.ENTER)
		time.sleep(2)
		self.driver.find_element(By.CSS_SELECTOR,'textarea + button').click()
		svg_path = 'M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15'
		try:
			WebDriverWait(self.driver, 60).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, f'[d="{svg_path}"]'))
			)
		except:
			input('>>> Bot check please notify when done!...')
			WebDriverWait(self.driver, 60).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, f'[d="{svg_path}"]'))
			)
		time.sleep(5)
		if self.name is None: # first ChatGPT instance ever or new is pressed and we are already at new
			self.name = self.run_script('chat.openai.get current chat name')()
			return self.run_script('chat.openai.get last answer')(), self
		elif newChat:
			name = self.run_script('chat.openai.get current chat name')()
			return self.run_script('chat.openai.get last answer')(), ChatGPT(self.driver,self.window,name)
		else:
			return self.run_script('chat.openai.get last answer')(), self