from django.shortcuts import render
from . import models
import openai,os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
api_key = os.getenv("OPENAI_KEY",None)
openai.api_key = api_key 


def Index(request): 
    all_questions = models.RandQ.objects.all()
    dict = {"questions":all_questions}
    response = None
    if api_key is not None and request.method == 'POST':
        question = request.POST.get('user_input')
        print(question)
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question,
            max_tokens = 256,
            #stop = ".",
            temperature = 0.5,
        )
        #response = "respuesta prueba"
        chatgpt_response = response["choices"][0]["text"]
        dict["response"] = chatgpt_response
        dict["questionAsked"] = question
    return render(request,"gptApp/Index.html",context=dict)  


def AnimalsQ(request): 
    all_questions = models.AnimalsQ.objects.all()
    dict = {"questions":all_questions}
    response = None
    if api_key is not None and request.method == 'POST':
        question = request.POST.get('user_input')
        print(question)
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question,
            max_tokens = 256,
            #stop = ".",
            temperature = 0.5,
        )
        #response = "respuesta prueba"
        chatgpt_response = response["choices"][0]["text"]
        dict["response"] = chatgpt_response
        dict["questionAsked"] = question
    return render(request,"gptApp/Animals.html",context=dict)  
