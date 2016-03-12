from django.conf.urls import include, url
from .views import *

urlpatterns = [
    # The main page for category
    url(r'^$', login, name='upperclassman_login'),
    
    # closed
    # url(r'^$', closed, name='upperclassman_login'),
    url(r'^list/', selection, name='selection'),
]