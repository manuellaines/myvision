from django.db import models

# Create your models here.
class Artist(models.Model):
    name=models.CharField(max_length=200,unique=True)
class Contact(models.Model):
    email=models.EmailField(max_length=100 unique=True)
    name=models.CharField(max_length=200)
class Album(models.Model):
    reference=models.IntegerField(null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    available=models.BooleanField(default=True)
    title=models.CharField(max_length=200)
    pictuare=models.URLField()
    artist=models.ManyToManyField(Artist)
class Booking(models.Model):
    create_at=models.DateTimeField(auto_now_add=True)
    contacted=models.BooleanField(default=False)
    Contact=models.ForeignKey(Contact,on_delete=models.CASCARDE)
    album=models.OneToOneField(Album,related_name='albums',blank=True)