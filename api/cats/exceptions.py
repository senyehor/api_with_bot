class CatsBaseException(Exception):
    message: str = None

    def __init__(self, message: str = None):
        # __class__.message allows to provide a default message in a subclass declaration
        self.message = message or self.__class__.message


class NotEnoughCats(CatsBaseException):
    message = 'there are not enough cats'
