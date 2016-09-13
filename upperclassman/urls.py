from django.conf.urls import include, url
from .views import *

urlpatterns = [
    # The main page for category
    # url(r'^$', upperclassman_closed, name='upperclassman'),
    url(r'^$', upper, name='upperclassman'),
]
