from abc import ABC, abstractmethod
from typing import Iterator, Any
from selenium import webdriver


class Feed(ABC):
    def __init__(self, name: str, driver: webdriver.Chrome, handle: str | None = None):
        self.name = name
        self.handle = handle
        self.driver = driver
        self.handle = driver.current_window_handle if handle is None else handle

    def focus(self):
        self.driver.switch_to.window(self.handle)

    @abstractmethod
    def __iter__(self) -> Iterator[Any]:
        pass
