from django.urls import path
from . import views
#to use django url names
app_name = 'cars'

urlpatterns = [
    path('list/',views.list,name='list'),
    path('add/',views.add,name='add'),
    path('delete/',views.delete,name='delete'),


]