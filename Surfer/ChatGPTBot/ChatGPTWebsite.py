
import selenium.webdriver as webdriver
# from Feed import Feed
from selenium import webdriver

from ..ScriptRunner import ScriptRunner
from .ChatGPT import ChatGPT


class ChatGPTWebsite:
	def __init__(self, driver:webdriver.Chrome,skip=True,handle:str|None=None,verbose=False,newWindow=True):
		self.name = 'GPT'
		self.handle = handle
		self.driver = driver
		self.verbose = verbose
		self.run_script = ScriptRunner(driver,'./Surfer/scripts/')
		if newWindow:
			self.parent_handle = driver.current_window_handle
			driver.switch_to.new_window()
			self.handle = driver.current_window_handle
		if not skip:
			self.driver.get('https://chat.openai.com/')
			self.handle = self.driver.current_window_handle
			self.run_script('surfer.listen to clicks')()
	def getLandingNewChat(self):
		return ChatGPT(self.driver,self)
	def focus(self):
		if self.handle is not None:
			self.driver.switch_to.window(self.handle)
