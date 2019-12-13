from django.conf.urls import url
from  . impolrt views
urlpatterns=[
    url(r'^$',views.landing_page, name ='landingPage'),
    
]