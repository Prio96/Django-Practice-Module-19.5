from django.db import models
from Musician.models import Musician
# Create your models here.
class Album(models.Model):
    album=models.CharField(max_length=255)
    musician=models.ForeignKey(Musician,on_delete=models.CASCADE,related_name="album")
    release_date=models.DateField(auto_now_add=True)
    