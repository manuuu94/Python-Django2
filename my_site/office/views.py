from django.shortcuts import render
from . import models

# Create your views here.

def ListView(request):
    all_patients = models.Patient.objects.all()
    dir = {'patients':all_patients}
    return render(request,'office/listview.html',context=dir)

   

