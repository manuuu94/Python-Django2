from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
  

class Personal(models.Model):
    name = models.CharField(max_length=60)
    middleName = models.CharField(max_length=60)
    lastName1 = models.CharField(max_length=60)
    lastName2 = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    birthDate = models.DateField()
    img = models.ImageField(upload_to='my_cv/static/my_cv/img')
    address = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.name} {self.middleName} {self.lastName1} {self.lastName2}"


class Languages(models.Model):
    language = models.CharField(max_length=60)
    level = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.language} - {self.level}"