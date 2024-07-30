from django.utils.translation import gettext as _
from rest_framework.generics import ListAPIView

from cats.logic import DEFAULT_CATS_AMOUNT, parse_int, RandomCatsQuerier
from cats.models import Cat
from cats.serializers import CatSerializer


class RandomCatsListView(ListAPIView):
    serializer_class = CatSerializer
    cats_querier = RandomCatsQuerier(Cat)

    def get_queryset(self):
        cats_amount = self.__extract_cats_amount_to_query()
        return self.cats_querier.get_random_cats(cats_amount, fail_on_not_enough_cats=False)

    def __extract_cats_amount_to_query(self):
        if cats_amount := self.request.GET.get('cats_amount', None):
            return parse_int(cats_amount, _('the cats_amount you provided failed to parse'))
        return DEFAULT_CATS_AMOUNT
