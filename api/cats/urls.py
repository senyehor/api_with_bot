from django.urls import path

from cats.views import docs, RandomCatsListView

urlpatterns = [
    path('random-cats', RandomCatsListView.as_view(), name='random-cats'),
    path('docs', docs, name='docs'),
]
