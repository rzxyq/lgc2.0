from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    # The main page for category
    url(r'^$', fresh),

    # When closed, replace above line with code below
    # url(r'^$', newstudent_closed)
)
