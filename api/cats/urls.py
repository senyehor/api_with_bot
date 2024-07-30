from django.urls import path

from cats.views import RandomCatsListView

urlpatterns = [
    path('random-cats', RandomCatsListView.as_view(), name='random-cats')
]
