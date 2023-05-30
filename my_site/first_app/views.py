from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def simple_view(request):
    return HttpResponse("Simple View")


def home_view(request):
    return HttpResponse("HOME VIEW")



#implementing dictionaries into views: 
articles = {
    'Sports':'Sports Page!',
    'Finance':'Finance Page!',
    'Arts':'Arts Page!',
    'Sports2':'New Sports2 Page!',
    'Arts2':'Arts2 Page!',

}

#static routing
def sports_view(request):
    return HttpResponse(articles['Sports'])


def finance_view(request):
    return HttpResponse(articles['Finance'])


#dynamic routing using dictionary
def news_views(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        #result = "No article found"
        #return HttpResponseNotFound(result)
        raise Http404("404 dumbass") 



def add_view(request,num1,num2):
    add = num1+num2
    result = f"{num1}+{num2}={add}"
    return HttpResponse(str(result))



def num_page_view(request,num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    #return HttpResponseRedirect(topic)

    webpage = reverse("topic-page",args=[topic]) #reverse method and args : always create a list for args even if its just one. 
    return HttpResponseRedirect(webpage)



def html_view(request):
    return render(request,'first_app/example.html') #where the template is

def html_view2(request):
    return render(request,'first_app/example2.html') #where the template is