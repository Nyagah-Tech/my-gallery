from django.db import models

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = model.EmailField()

class Gallery(models.Model):
    description = models.TextField()
    name = models.CharField(max_length = 50)
    owner = models.ForeignKey(Owner, on_delete = models.CACSCADE)
    picture = models.ImageField()
    
