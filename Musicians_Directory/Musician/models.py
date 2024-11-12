from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    instrument_type=models.CharField(max_length=50)

    