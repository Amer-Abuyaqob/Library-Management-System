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