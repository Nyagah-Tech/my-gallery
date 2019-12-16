from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.landing_page, name ='landingPage'),
    path('images/<int:id>',views.image_section,name = 'image-section'),
    path('category/<int:id>' ,views.category,name ='category'),
    path('location/<int:id>',views.location,name='location'),
    path('search/',views.search_term,name="results")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
