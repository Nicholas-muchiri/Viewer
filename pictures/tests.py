from .models import Location, Category, Picture
from django.test import TestCase

# Create your tests here.


class CategoryTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.cars = Category(picture_category='cars')
        self.cars.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.cars,Category))
    
    def tearDown(self):
        self.cars.delete_category()
    
    def test_updating_category(self):
        category = Category.get_category_id(self.cars.id)
        category.update_category('SUV')
        category = Category.get_category_id(self.cars.id)
        self.assertTrue(category.photo_category == 'SUV')
    