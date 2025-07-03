"""
Reservable Interface Module

This module defines the Reservable abstract interface that provides
reservation functionality for library items.

The Reservable interface defines:
- A property to check if an item is reserved and by whom
- A method to reserve an item for a specific user

This interface is implemented by Book and DVD classes, allowing these
item types to be reserved by users. Magazines do not implement this
interface and cannot be reserved.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from user import User


class Reservable(ABC):
    """
    Abstract interface for objects that can be reserved by a user.
    
    This interface defines the contract for reservation functionality
    in the library system. Classes that implement this interface can
    be reserved by users, allowing them to claim items before borrowing.
    
    The interface ensures that:
    - Items can track who has reserved them
    - Items can be reserved by a specific user
    - The reservation status can be queried
    
    Currently implemented by Book and DVD classes.
    """

    @property
    @abstractmethod
    def reserved_by(self) -> Optional[User]:
        """
        Get the user who has reserved this item.
        
        Returns the user who currently has this item reserved, or None
        if the item is not currently reserved.
        
        Returns:
            User or None: The user who has reserved the item, or None if not reserved
        """
        pass

    @abstractmethod
    def reserve(self, user: User) -> None:
        """
        Reserve the item for a specific user.
        
        Marks the item as reserved by the specified user. Only one user
        can reserve an item at a time. If the item is already reserved,
        this method will overwrite the previous reservation.
        
        Args:
            user (User): The user who is reserving the item
        """
        pass
