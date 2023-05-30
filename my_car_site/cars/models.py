from django.db import models

# Create your models here.
class Car(models.Model):
    #PK is not necessary to add it. djang implements it.
    brand = models.CharField(max_length=30)
    year = models.IntegerField()


    def __str__(self):
        return f"Car ID: {self.id} - is a {self.brand} {self.year}"