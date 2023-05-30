from django.http.response import HttpResponse
from django.shortcuts import render

def home_view2(request): 
    return HttpResponse("HOME VIEW!")


def home_view(request):
    return render(request,'base.html')



