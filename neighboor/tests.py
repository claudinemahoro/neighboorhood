from django.test import TestCase

# Create your tests here.
from .models import *
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    def setUp(self):
        self.coco = Profile( user = 'coco', profile_picture  = '/', bio = 'my tests', contact='mahorotesting@gmail.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.coco,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.coco.save_profile()
        coco = Profile.objects.all()
        self.assertTrue(len(coco) > 0)

    def tearDown(self):
        Profile.objects.all().delete()
       
class Neighbourhood(TestCase):
    '''
    Test case for the Neighbourhood class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create a Image instance
        self.new_Image = Image(
            caption='Python check 123')

    def test_instance(self):
        '''
        Test case to check if self.new_Image in an instance of Image class
        '''
        self.assertTrue(isinstance(self.new_Image, Image))

class Post(TestCase):
    '''
    Test case for the Comment class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Comment class
        '''
        # Create a Comment instance
        self.new_comment = Comment(
            comment_content='Python check 123')

    def test_instance(self):
        '''
        Test case to check if self.new_comment in an instance of Comment class
        '''
        self.assertTrue(isinstance(self.new_comment, Comment))

class Business(self):
    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create a Business instance
        self.new_bus = Bus(
            name='Salesman')
    @classmethod
    def get_specific_bus(cls,id):
        '''
        fetches particular hooddeletes an exiting neighborhood
        '''
        business = cls.objects.filter(id=id)
        return business
