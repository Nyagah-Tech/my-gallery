from django.test import TestCase
from .models import Gallery,Category,Location,Owner

class Owner(TestCase):
    def setUp(self):
        self.dan = Owner(first_name = 'dan',last_name ='nyagah',email='dan@gmail.com',phone_number ="0712345678")
    def test_instance(self):
        self.assertTrue(isinstance(self.dan,Owner))
class Gallery(TestCase):
    def setUp(self):
    # creating a new picture and saving it
        self.new_picture = Gallery(description ="i am a test",name ="test" ,owner="dan",picture="image",location="ngong",category="kampala",posted_by ="1/12/2019")
        self.new_picture.save()
        #creating a location and saving it
        self.new_location = Location(location ="ngong")
        self.new_location.save()
        #creating a category and saving it
        self.new_category=Category(category = "food")
        self.new_category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_picture,Gallery))
    def test_get_all_images():
        images = get_all_images()
        self.assertTrue(len(images) > 0)
    def test_get_images_by_location():
        self.new_picture.save()
        image = get_images_by_location(ngong)
        self.assertTrue(image,self.new_picture)
    def test_get_image_by_name():
        self.new_picture.save()
        image = get_image_by_name(test)
        self.assertTrue(image,self.new_picture)
    def test_delete():
        self.new_picture.save()
        image = get_image_by_name(test)
        images = get_all_images()
        images.delete()
        self.assertTrue(len(images)==0)
    def test_get_all_categories():
        self.new_category.save()
        category = get_all_categories()
        self.assertTrue(len(category)==1)
    def test_get_all_location():
        self.new_location.save()
        location = get_all_locations()
        self.assertTrue(len(location)==1)


class Location(TestCase):
    def setUp(self):
        self.location = Location(location = "ngong")
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
class Category(TestCase):
    def setUp(self):
        self.category = Category(category = "food")
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

# Create your tests here.
