import random
import time
from typing import Any, Iterator

import selenium.webdriver as webdriver

from ..Feed import Feed
from ..util import N


class RedditPostFeed(Feed):
	def __init__(self, driver:webdriver.Chrome ,handle:str|None=None,verbose=False):
		super().__init__(name='Reddit Post Feed',driver=driver,handle=handle)
		# Store the WebDriver instance
		self.verbose = verbose
		self.focus()
		self.run_script('surfer.listen to clicks')()
		self.run_script('reddit.catch first comment',self.verbose)()

	def __iter__(self) -> Iterator[Any]:
		while True:
			self.focus()
			if not self.run_script('surfer.check cursor',verbose=self.verbose)():
				self.run_script('reddit.post.catch first comment',verbose=self.verbose)()
				continue
			self.run_script('surfer.scroll 2 cursor',verbose=self.verbose)(N(bounds=[0,1]),N(bounds=[0,1]),random.randint(1,25)/100)
			for i in range(10):
				if self.run_script('surfer.check still scrolling')():
					time.sleep(0.1)
				else:
					break
				if i == 9:
					raise Exception('Not finished scrolling')
			yield self.run_script('reddit.post.parse comment',verbose=self.verbose)()
			self.run_script('reddit.post.cursor next')()
