from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.


def my_cv(request):
    personalData = models.Personal.objects.get(pk=1)
    name = personalData
    phone = personalData.phone
    email = personalData.email
    birthDate = personalData.birthDate
    address = personalData.address
    languages = models.Languages.objects.all()
    print(languages)
    dict = {"data":{"name":name,
            "phone":phone,
            "email":email,
            "birthDate":birthDate,
            "address":address},
            "languages":languages}
            
    return render(request,'my_cv/manucv.html',context = dict)