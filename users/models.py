from django.db import models

# Create your models here.
from django.core.validators import MaxLengthValidator
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# Create your models here.
