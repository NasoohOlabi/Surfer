from abc import ABC, abstractmethod
from typing import Any, Iterator

from selenium import webdriver

from .ScriptRunner import ScriptRunner


class Feed(ABC):
    def __init__(self, name: str, driver: webdriver.Chrome, handle: str | None = None):
        self.name = name
        self.handle = handle
        self.driver = driver
        self.handle = driver.current_window_handle if handle is None else handle
        self.run_feed_script = ScriptRunner(driver,'./Surfer/scripts/')

    def focus(self):
        if self.handle is not None:
            self.driver.switch_to.window(self.handle)

    @abstractmethod
    def __iter__(self) -> Iterator[Any]:
        pass
