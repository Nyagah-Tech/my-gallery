from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Gallery


# Create your views here.

def landing_page(request):
    date = dt.date.today()
    images = Gallery.get_all_images()

    return render(request,'display-images/landing.html',{"date":date,"images":images})

def image_section(request,image_id):
    image =Gallery.get_image_by_id(image_id)

    return render(request, 'display-images/image.html',{"image":image} )