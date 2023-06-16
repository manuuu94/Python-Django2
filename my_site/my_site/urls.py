"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
#from django.http.response import HttpResponse
from . import views


#def home_view(request): #these functions may be created in a different file/folder specific for the home page. 
#    return HttpResponse("HOME VIEW")

urlpatterns = [
    path('my_app/', include('my_app.urls')), #django recognizes there's a my_app app with a .urls folder. 
    path('first_app/',include('first_app.urls')),
    #path('',views.home_view2),
    path('',views.home_view,name='base'),
    path('admin/', admin.site.urls),
    path('office/',include('office.urls')),
    path('cars/',include('cars.urls')),
    path('classroom/',include('classroom.urls')),
]
#the PAGE NOT FOUND will show them in this order as it is in URLPATTERNS. DEBUG = TRUE

#kwargs: allows us to pass in keyword arguments as a dictionary to the view. 
#name: allows u to name a URL in morder to reference it elsewhere in Django. 

#runserver will show the existing paths if DEBUG = TRUE in settings.




