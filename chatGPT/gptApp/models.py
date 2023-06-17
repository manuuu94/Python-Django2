from django.db import models

# Create your models here.



class RandQ(models.Model):
    question = models.CharField(max_length=200,null=True,blank=True)
    answer = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return f"{self.question}"
    

class AnimalsQ(models.Model):
    question = models.CharField(max_length=200,null=True,blank=True)
    answer = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return f"{self.question}"


class MathQ(models.Model):
    question = models.CharField(max_length=200,null=True,blank=True)
    answer = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return f"{self.question}"