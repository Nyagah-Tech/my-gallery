from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
import pyperclip
from .models import Gallery,Category,Location


# Create your views here.

def landing_page(request):
    date = dt.date.today()
    images = Gallery.get_all_images()
    locations = Location.get_all_locations()
    category = Category.get_all_categories()
    return render(request,'display-images/landing.html',{"date":date,"images":images,"category":category,"locations":locations})

def image_section(request,id):
    image =Gallery.get_image_by_id(id)
    locations = Location.get_all_locations()
    category = Category.get_all_categories()

    return render(request, 'display-images/image.html',{"image":image,"category":category,"locations":locations})
