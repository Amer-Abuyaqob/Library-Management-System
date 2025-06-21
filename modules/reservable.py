from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from user import User


class Reservable(ABC):
    """Interface for objects that can be reserved by a user."""

    @property
    @abstractmethod
    def reserved_by(self) -> Optional[User]:
        """Return the user who reserved this item, if any."""

    @abstractmethod
    def reserve(self, user: User) -> None:
        """Reserve the item for ``user``."""

