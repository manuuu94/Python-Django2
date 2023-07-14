from django.shortcuts import redirect, render
from . import models
from chatGPT.views import categories, addCategory
import openai,os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
api_key = os.getenv("OPENAI_KEY",None)
openai.api_key = api_key 


def allQuestions(request):
    dict = {}
    if request.method == 'POST' and request.POST.get('inputnav'):       
        print("yes")
        return redirect('gptApp:AllQuestions')

#this is to be able to add and show all categories from every tab in the navbar
    if request.method == 'POST' and request.POST.get('input'):
        addCategory(request)
        return redirect('gptApp:AllQuestions')
    dict["categories"] = categories()
    return render(request,'gptApp/AllQuestions.html', context = dict)

    
        

