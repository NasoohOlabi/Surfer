
import logging
import os
import random
import sys
import time
from typing import Callable

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


def GetBrowser(browser=None, time_out=600):
    chrome_options = Options()
    if sys.platform == "win32":
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--user-data-dir=C:/Temp/ChromeProfile")
        chrome_options.add_argument("--disable-gpu")
    else:
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--user-data-dir=./User_Data")
    if not browser:
        ChromeDriverManager().install()
        browser = webdriver.Chrome(chrome_options)

        handles = browser.window_handles
        for _, handle in enumerate(handles):
            if handle != browser.current_window_handle:
                browser.switch_to.window(handle)
                browser.close()

    return browser
