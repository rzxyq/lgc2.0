from django.conf.urls import include, url
from .views import *

urlpatterns = [
    # The main page for category
    url(r'^$', basic, name='newstudent'),
    # When closed, replace above line with code below
    # url(r'^$', newstudent_closed)
   
    # The main page for each individual category page
    # url(r'^academic/', academic),
    # url(r'^extracurricular/', extracurricular),
    # url(r'^career/', career),
    # url(r'^shortanswer/', shortanswer),
]
