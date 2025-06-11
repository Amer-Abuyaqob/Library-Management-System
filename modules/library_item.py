from abc import ABC, abstractmethod

class LibraryItem(ABC):
    # FIXME: add the attributes for [LibraryItem]
    def __init__(self) -> None:
        # FIXME: initialize the attributes of [LibraryItem]
        super().__init__()

    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def check_availability(self):
        pass