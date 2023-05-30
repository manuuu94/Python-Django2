from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinLengthValidator(20),MaxLengthValidator(300)])
    heartrate = models.IntegerField(default=60,validators=[MinLengthValidator(20),MaxLengthValidator(300)])

    def __str__(self): #define the str of the object, otherwise it prints only its memory space reference
        return f"{self.first_name} {self.last_name} {self.age} {self.heartrate}"
    
