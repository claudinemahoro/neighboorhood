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

