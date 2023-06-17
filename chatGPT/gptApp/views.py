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
    #print(all_questions)
    dict = {"questions":all_questions}
    response = None
    if api_key is not None and request.method == 'POST':
        question = request.POST.get('user_input')
        #print(question)
        obj = models.RandQ.objects.get(question=question)
        #print(obj.answer) 
        if obj.answer is None:
            response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question,
            max_tokens = 256,
            #stop = ".",
            temperature = 0.5,
            )
            chatgpt_response = response["choices"][0]["text"]
            dict["response"] = chatgpt_response
            dict["questionAsked"] = question 
            obj.answer = chatgpt_response
            obj.save()
            #print(obj.answer)
            return render(request,"gptApp/Index.html",context=dict)        
        dict["response"] = obj.answer   
        dict["questionAsked"] = question
    return render(request,"gptApp/Index.html",context=dict)  


def AnimalsQ(request): 
    all_questions = models.AnimalsQ.objects.all()
    #print(all_questions)
    dict = {"questions":all_questions}
    response = None
    if api_key is not None and request.method == 'POST':
        question = request.POST.get('user_input')
        #print(question)
        obj = models.AnimalsQ.objects.get(question=question)
        #print(obj.answer) 
        if obj.answer is None:
            response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question,
            max_tokens = 256,
            #stop = ".",
            temperature = 0.5,
            )
            chatgpt_response = response["choices"][0]["text"]
            dict["response"] = chatgpt_response
            dict["questionAsked"] = question 
            obj.answer = chatgpt_response
            obj.save()
            #print(obj.answer)
            return render(request,"gptApp/Animals.html",context=dict)        
        dict["response"] = obj.answer   
        dict["questionAsked"] = question
    return render(request,"gptApp/Animals.html",context=dict)  


def MathQ(request): 
    all_questions = models.MathQ.objects.all()
    #print(all_questions)
    dict = {"questions":all_questions}
    response = None
    if api_key is not None and request.method == 'POST':
        question = request.POST.get('user_input')
        #print(question)
        obj = models.MathQ.objects.get(question=question)
        #print(obj.answer) 
        if obj.answer is None:
            response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question,
            max_tokens = 256,
            #stop = ".",
            temperature = 0.5,
            )
            chatgpt_response = response["choices"][0]["text"]
            dict["response"] = chatgpt_response
            dict["questionAsked"] = question 
            obj.answer = chatgpt_response
            obj.save()
            #print(obj.answer)
            return render(request,"gptApp/Math.html",context=dict)        
        dict["response"] = obj.answer   
        dict["questionAsked"] = question
    return render(request,"gptApp/Math.html",context=dict)  


