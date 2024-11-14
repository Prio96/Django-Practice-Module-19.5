from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from Musician.models import Musician
# Create your models here.
class Rating(models.IntegerChoices):
    one=1,'1'
    two=2,'2'
    three=3,'3'
    four=4,'4'
    five=5,'5'
class Album(models.Model):
    title=models.CharField(max_length=255)
    musician=models.ForeignKey(Musician,on_delete=models.CASCADE,related_name="albums")  
    release_date=models.DateField(auto_now_add=True)
    rating=models.PositiveSmallIntegerField(
        choices=Rating.choices,
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    def __str__(self):
        return self.title
    