from typing import Generic, Iterable, TypeVar

from django.db.models import Model

from cats.exceptions import FailedToParseInt, NotEnoughCats

DEFAULT_CATS_AMOUNT = 5

CatModelType = TypeVar('CatModelType', bound=Model)


class RandomCatsQuerier(Generic[CatModelType]):
    def __init__(self, cats_model: type[CatModelType]):
        self.__cats_model = cats_model

    def get_random_cats(
            self, amount: int, fail_on_not_enough_cats: bool = False
    ) -> Iterable[CatModelType]:
        # django default random ordering is very inefficient, but does the job here
        if amount < 0:
            raise ValueError('positive number must be provided')
        if self.__check_there_are_enough_cats(amount):
            if fail_on_not_enough_cats:
                raise NotEnoughCats
        return self.__cats_model.objects.order_by('?').all()[:amount]

    def __check_there_are_enough_cats(self, amount: int):
        cats_count = self.__cats_model.objects.count()
        if cats_count == 0:
            raise NotEnoughCats
        return cats_count < amount


def parse_int(data: str, message_on_fail: str) -> int:
    try:
        return int(data)
    except ValueError as e:
        raise FailedToParseInt(message_on_fail) from e
