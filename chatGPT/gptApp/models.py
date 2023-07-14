from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.categoryName}"
    
class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=500)
    categoryId = models.IntegerField()
    answer = models.CharField(max_length=500, blank=True,null=True)

    def __str__(self):
        return f"{self.question}"
     

