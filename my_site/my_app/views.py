from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hellooooo! This is the view inside my_app")



def index2(request):
    return HttpResponse("Hellooooo! this is another view")



def example_view(request):
    return render(request,'my_app/example.html') #location of the template. 


def variable_view(request):

    my_var = {'first_name':'manuel','last_name':'gonzález',
              'list':[0,1,2,3,4],
              "dict":{'dict_ins_key':'manu_inside_value',
                      'dict_ins_key2':'manu_inside_value2'}
              }   
    return render(request,'my_app/variables.html',context = my_var)


#template inheritance is to not repeat the same html code in every template, such as a navbar. 










