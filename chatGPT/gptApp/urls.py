from django.urls import path
from . import views


app_name = 'gptApp'

urlpatterns = [
    path('',views.Index,name='Index'),
    path('animals/',views.AnimalsQ,name='animals'),
    path('math/',views.MathQ,name='math'),
]