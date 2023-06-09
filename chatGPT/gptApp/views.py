from django.shortcuts import render
from . import models

# Create your views here.

def Index(request): 
    all_questions = models.RandQ.objects.all()
    dict = {"questions":all_questions}
    return render(request,"gptApp/Index.html",context=dict)  
