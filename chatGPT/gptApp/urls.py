from django.urls import path
from . import views


app_name = 'gptApp'

urlpatterns = [
    path('',views.Index,name='Index'),
]