class User:
    """Represents a library user."""

    def __init__(self, user_id: str, first_name: str, last_name: str) -> None:
        """Initialize a new ``User``.

        Parameters
        ----------
        user_id:
            Unique identifier for the user.
        first_name:
            User's first name.
        last_name:
            User's last name.
        """

        self._id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__borrowed_items: list[str] = []

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------
    @property
    def id(self) -> str:
        return self._id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def borrowed_items(self) -> list[str]:
        return list(self.__borrowed_items)

    # ------------------------------------------------------------------
    # Convenience methods
    # ------------------------------------------------------------------
    def borrow_item(self, item_id: str) -> bool:
        """Register ``item_id`` as borrowed by the user."""
        if item_id in self.__borrowed_items:
            return False
        self.__borrowed_items.append(item_id)
        return True

    def return_item(self, item_id: str) -> bool:
        """Remove ``item_id`` from the borrowed items list."""
        if item_id not in self.__borrowed_items:
            return False
        self.__borrowed_items.remove(item_id)
        return True

