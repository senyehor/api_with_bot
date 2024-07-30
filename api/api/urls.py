from django.conf.urls.static import static
from django.urls import include, path

from api.settings import DEBUG, STATIC_URL

urlpatterns = [
    path('api/', include('cats.urls')),

]

if DEBUG:
    urlpatterns += static(STATIC_URL)
