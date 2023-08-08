
import logging
import os
import random
import sys
import time
from typing import Callable

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException,
                                        UnexpectedAlertPresentException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import _element_if_visible
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class invisibility_of(object):
    def __init__(self, element):
        self.element = element

    def __call__(self, ignored):
        return not _element_if_visible(self.element)

load_dotenv()

def GetBrowser(browser=None, time_out=600):
    chrome_options = Options()
    if sys.platform == "win32":
        udd = os.getenv('user-data-dir')
        if udd is not None:
            chrome_options.add_argument("--user-data-dir="+udd)
            chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--disable-gpu")
    else:
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--user-data-dir=./User_Data")
    if not browser:
        browser = webdriver.Chrome(chrome_options)
    browser.implicitly_wait(2)
    return browser

browser = None
if __name__ == '__main__':
    browser = GetBrowser()