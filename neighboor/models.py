from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class NeighbourHood(models.Model):
    name = models.CharField(max_length =30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="neighbor")
    location = models.CharField(max_length =30)
    cover = models.ImageField(upload_to='pic/')
    health_tell = models.IntegerField()
    police_number = models.IntegerField()

    def __str__(self):
        return self.name

    @classmethod
    def get_specific_hood(cls,id):
        hood = cls.objects.get(id=id)
        return hood


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete() 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500)
    contact = models.CharField(max_length=200)
   
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    # neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')
    # user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    @classmethod
    def get_specific_bus(cls,id):
        bus = cls.objects.get(id=id)
        return bus



