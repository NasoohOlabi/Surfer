import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Literal, Optional

from .Person import Person


@dataclass
class Message:
    person: Person
    text: str
    _time: Optional[datetime] = field(init=False,default=None)

    def __post_init__(self):
        self._time = datetime.now()

    @property
    def time(self) -> datetime:
        return self._time # type: ignore

    def __str__(self):
        return json.dumps({
            'person': f"{self.person.first_name} {self.person.last_name}",
            'text': self.text,
            'time': self.time.strftime('%Y-%m-%d %H:%M:%S') 
        })

    def __repr__(self):
        return self.__str__()
