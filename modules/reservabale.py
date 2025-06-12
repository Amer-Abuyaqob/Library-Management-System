from abc import ABC, abstractmethod
from user import User

class Reservable(ABC):
    # FIXME: add the attributes for [Reservable]
    def __init__(self):
        # FIXME: initialize the attributes of [Reservable]
        super().__init__()

    @abstractmethod
    def reserve(self, user: User):
        pass