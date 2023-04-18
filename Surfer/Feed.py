from abc import ABC, abstractmethod
from typing import Iterator, Any

class Feed(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def __iter__(self) -> Iterator[Any]:
        pass
