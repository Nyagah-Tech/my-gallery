from django.db import models
import datetime as dt

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank = True)


    def __str__(self):
        return self.first_name

class Location(models.Model):
    location = models.CharField(max_length = 50)

    @classmethod
    def get_all_locations(cls):
        locations = cls.objects.all()
        return locations

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length = 100)

    @classmethod
    def get_all_categories(cls):
        categories = cls.objects.all()
        return categories
    @classmethod
    def get_category_by_id(cls,category_id):
        category = cls.objects.filter(id = category_id)
        return category


    def __str__(self):
        return self.category


class Gallery(models.Model):
    description = models.TextField()
    name = models.CharField(max_length = 50)
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    picture = models.ImageField(upload_to = 'images/')
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    posted_by = models.DateTimeField(dt.datetime.now())

    def delete(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()

        return images
    
    @classmethod
    def get_images_category(cls,categorys):
        images = cls.objects.filter(category = categorys)

        return images

    @classmethod
    def get_images_by_location(cls,locations):
        images = cls.objects.filter(location = locations)

        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id = id)

        return image
    @classmethod
    def get_image_by_name(cls,name):
        image = cls.objects.filter(name = name)
        return image


    def __str__(self):
        return self.name


