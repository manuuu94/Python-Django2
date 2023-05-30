from django.shortcuts import redirect, render
from django.urls import reverse
from . import models

# Create your views here.

def Index(request):
    
    return render(request,"cars/index.html")


def ListCar(request):
    all_cars = models.Car.objects.all()
    dict = {"cars":all_cars}
    return render(request,"cars/list.html",context=dict)


def AddCar(request):
    #print(request.POST)
    if request.POST:
        brand = request.POST['brand']
        year = request.POST['year']
        models.Car.objects.create(brand=brand,year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request,"cars/add.html")


def DeleteCar(request):
    if request.POST:
        pkid = request.POST['pkid']
        try: 
            models.Car.objects.get(pk=pkid).delete()
            return redirect(reverse('cars:list'))
        except:
            print("Not found")
            return redirect(reverse('cars:delete'))
    else:
        return render(request,"cars/delete.html")









