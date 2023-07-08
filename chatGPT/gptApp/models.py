from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.categoryName}"
    
class Question(models.Model):
    question = models.CharField(max_length=500)
    categoryId = models.IntegerField()

    def __str__(self):
        return f"{self.question}"
     

#######
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


class EnvironmentQ(models.Model):
    question = models.CharField(max_length=200,null=True,blank=True)
    answer = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return f"{self.question}"        


class HealthQ(models.Model):
    question = models.CharField(max_length=200,null=True,blank=True)
    answer = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return f"{self.question}"     


class AnatoQ(models.Model):
    question = models.CharField(max_length=200,null=True,blank=True)
    answer = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return f"{self.question}"     