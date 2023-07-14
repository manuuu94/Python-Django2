from django.urls import path
from . import views


app_name = 'gptApp'

urlpatterns = [
    path('questions/',views.allQuestions,name='AllQuestions'),


]



