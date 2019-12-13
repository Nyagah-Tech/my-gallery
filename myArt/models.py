from django.db import models
import datetime as dt

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()


    def __str__(self):
        return self.first_name

class Location(models.Model):
    location = models.CharField(max_length = 50)

class Category(models.Model):
    category = models.CharField(max_length = 100)

class Gallery(models.Model):
    description = models.TextField()
    name = models.CharField(max_length = 50)
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    picture = models.ImageField()
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    posted_by = models.DateTimeField(dt.datetime.now())


    def __str__(self):
        return self.name


