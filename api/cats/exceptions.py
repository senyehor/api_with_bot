from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.exceptions import APIException


class CatsBaseException(APIException):
    pass


class NotEnoughCats(CatsBaseException):
    status_code = status.HTTP_204_NO_CONTENT
    default_detail = _('Not enough cats to fulfill request')


class FailedToParseInt(CatsBaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('failed to parse an integer value you provided')
