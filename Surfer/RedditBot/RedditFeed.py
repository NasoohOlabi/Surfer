import random
import time
from typing import Any, Iterator

import selenium.webdriver as webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..Feed import Feed
from ..util import N, uuid
from .RedditPostFeed import RedditPostFeed


class RedditFeed(Feed):
	def __init__(self, driver:webdriver.Chrome,skip=True,handle:str|None=None,verbose=False,subreddit:str|None=None,newWindow=True):
		super().__init__(name='Reddit Feed',handle=handle,driver=driver)
		self.verbose = verbose
		if newWindow:
			self.parent_handel = driver.current_window_handle
			driver.switch_to.new_window()
			self.handle = driver.current_window_handle
		if not skip:
			self.driver.get('https://www.reddit.com/'+ (f'r/{subreddit}/' if subreddit is not None else ''))
			self.handle = self.driver.current_window_handle
			self.run_script('surfer.listen to clicks')()
		self.run_script('reddit.init_reddit',verbose=self.verbose)()
	

	def __iter__(self) -> Iterator[Any]:
		while True:
			self.focus()
			if not self.run_script('surfer.check cursor',verbose=self.verbose)():
				continue
			self.run_script('surfer.scroll 2 cursor',verbose=self.verbose)(N(bounds=[0,1]),N(bounds=[0,1]),random.randint(1,25)/100)
			for i in range(10):
				if self.run_script('surfer.check still scrolling')():
					time.sleep(0.1)
				else:
					break
				if i == 9:
					raise Exception('Not finished scrolling')
			yield self.run_script('reddit.parse post',verbose=self.verbose)()
			self.run_script('surfer.cursor next')()

	def click_post(self, newTab=True):
		for i in range(10): # 10 retries
			self.focus()
			if i == 9:
				raise Exception('cursor not present')
			if not self.run_script('surfer.check cursor',verbose=self.verbose)():
				continue
			else:
				break
  
		id = uuid()
		self.run_script('surfer.mark cursor', verbose=self.verbose)(id)
		# Find the DOM element to click on
		sel = f'.{id}'
		element = self.driver.find_element(By.CSS_SELECTOR, sel)
		h3 = element.find_element(By.CSS_SELECTOR,'h3')
		element = element if h3 is None else h3
		actions = ActionChains(self.driver)
		actions \
			.click(element) \
			.perform()
			# .key_down(Keys.CONTROL) \
			# .key_up(Keys.CONTROL) \
		return RedditPostFeed(self.driver,self.handle,verbose=self.verbose)

	def close(self):
		self.focus()
		# Close the WebDriver instance
		self.driver.quit()
