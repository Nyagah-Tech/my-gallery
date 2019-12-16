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
def category(request,id):
    category = Category.get_all_categories()
    locations = Location.get_all_locations()
    images = Gallery.get_images_category(id)
    title = Category.get_category_by_id(id)

    return render(request, 'display-images/category.html',{ "title":title,"images":images,"category":category,"locations":locations})

def get_categories(request):
    category = Category.get_all_categories()
    locations = Location.get_all_locations()

    return render(request,'navbar.html',{"category":category,"locations":locations})

def location(request,id):
    category = Category.get_all_categories()
    locations = Location.get_all_locations()
    images = Gallery.get_images_by_location(id)
    return render(request,'display-images/location.html',{"images":images,"locations":locations,"category":category})

def copy(request,imageUrl):
    image_url = 'http://127.0.0.1:8000'
    base_url = imageUrl
    final_url = image_url + base_url
    date = dt.date.today()
    images = Gallery.get_all_images()
    locations = Location.get_all_locations()
    category = Category.get_all_categories()
    return render(request,'display-images/copy.html',{"date":date,"images":images,"category":category,"locations":locations,"final_url":final_url})
