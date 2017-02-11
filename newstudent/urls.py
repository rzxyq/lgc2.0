from django.conf.urls import include, url
from .views import *

urlpatterns = [
    # The main page for category
    url(r'^$', basic, name='newstudent'),
    
    # When closed, replace above line with code below
    # url(r'^$', newstudent_closed, name='newstudent')
]
