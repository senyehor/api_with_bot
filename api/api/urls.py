from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework.reverse import reverse_lazy

from api.settings import DEBUG, STATIC_URL

urlpatterns = [
    path('api/', include('cats.urls')),
    path('', RedirectView.as_view(url=reverse_lazy('docs')))
]

if DEBUG:
    urlpatterns += static(STATIC_URL)
