class User:
    def __init__(self, user_id, first_name, last_name):
        # TODO: auto generated user_id (U-FfLl-N)
        self._id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__borrowed_items = []

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def borrowed_items(self):
        return self.__borrowed_items

# FIXME: use exception handling instead of true/false
    def borrow_item(self, item_id):
        """Register ``item_id`` as borrowed by the user."""
        if item_id in self.__borrowed_items:
            return False
        self.__borrowed_items.append(item_id)
        return True

    def return_item(self, item_id):
        """Remove ``item_id`` from the borrowed items list."""
        if item_id not in self.__borrowed_items:
            return False
        self.__borrowed_items.remove(item_id)
        return True