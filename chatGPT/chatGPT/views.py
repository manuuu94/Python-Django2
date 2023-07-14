from django.shortcuts import render, redirect,reverse
import openai,os
from gptApp import models
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("OPENAI_KEY",None)
openai.api_key = api_key 



def chatGPT(request):
    dict = {}
    dict["categories"] = categories()
    if request.method == 'POST' and request.POST.get('delqtsbtn'):
        value = request.session.get(('idValue'),None)
        deleteAllQuestios(value)
        dict["questions"] = questions(request.session.get(('idValue'),None))
        return render(request,'gptApp/AllQuestions.html', context = dict)

    if request.method == 'POST' and request.POST.get('delctybtn'):
        value = request.session.get(('idValue'),None)
        deleteAllQuestios(value)
        deleteCategory(value)
        return redirect('chatGPT')
       
    if request.method == 'POST' and request.POST.get('addinput'):
        addQuestion(request)
        dict["questions"] = questions(request.session.get(('idValue'),None))
        return render(request,'gptApp/AllQuestions.html', context = dict)

    if request.method == 'POST' and request.POST.get('deletebtn'):
        deleteQuestion(request.POST.get('deletebtn'))
        dict["questions"] = questions(request.session.get(('idValue'),None))
        return render(request,'gptApp/AllQuestions.html', context = dict)
    
    if request.method == 'POST' and request.POST.get('editbtn'):
        editQuestion(request)
        dict["questions"] = questions(request.session.get(('idValue'),None))
        return render(request,'gptApp/AllQuestions.html', context = dict)
    if api_key is not None and request.method == 'POST' and request.POST.get('user_input'):
        api(request)
        return redirect('chatGPT')
    if request.method == 'POST' and request.POST.get('input'):
        addCategory(request)
        return redirect('chatGPT')
    dict["response"] = request.session.get('chatgpt_response',None)   
    if request.method == 'POST' and request.POST.get('inputnav'):   
        idValue = request.POST.get('inputnav')
        dict["id"] = idValue
        request.session['idValue'] = idValue
        dict["questions"] = questions(idValue)
        return render(request,'gptApp/AllQuestions.html', context = dict)
    
    if api_key is not None and request.method == 'POST' and request.POST.get('user_input2'):
        dict["questions"] = questions(request.session.get(('idValue'),None))
        apiAllQ(request)
        dict["response2"] = request.session.get('chatgpt_response2',None)
        dict["questionAsked"] = request.POST.get('user_input2')
        return render(request,'gptApp/AllQuestions.html', context = dict)
    return render(request,'chatGPT/main.html', context = dict)

def addQuestion(request):
    models.Question.objects.create(id=getEmptyId(),
    question=request.POST.get('addinput'),
    categoryId=request.session.get(('idValue'),None))

def getEmptyId():
    index = 1
    while len(models.Question.objects.filter(id=index).all()) > 0:
        index = index+1
    return index
            
def deleteQuestion(value):
    obj = models.Question.objects.get(id=value)
    obj.delete()

def questions(idValue):
    questions = models.Question.objects.filter(categoryId = idValue).all()
    dict = {}
    index = 0
    for question in questions:
        dict[f"question{index}"] = {"id":question.id, "question":question.question, "idCat":question.categoryId}
        index = index+1  
    return dict

def categories():
    categories = models.Category.objects.all()
    new_dict = {}
    for category in categories:
        new_dict[category.id] = {"id":category.id,"name":category.categoryName}    
    return new_dict

def countCategories():
    categories = models.Category.objects.all()
    index = 0
    for category in categories:
        index = index+1
    return index

def addCategory(request):
        name = request.POST.get('input')
        index = 0
        index = countCategories()+1
        models.Category.objects.create(id=index,categoryName=name)  
   
def api(request):
    chatgpt_response = None
    if api_key is not None and request.method == 'POST' and request.POST.get('user_input'):
        user_input = request.POST.get('user_input')  # user_input 
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = user_input,
            max_tokens = 256,
            #stop = ".",
            temperature = 0.5,
        )
        chatgpt_response = response["choices"][0]["text"]
        request.session['chatgpt_response'] = chatgpt_response

def apiAllQ(request):
    chatgpt_response = None
    if api_key is not None and request.method == 'POST' and request.POST.get('user_input2'):
        user_input = request.POST.get('user_input2')  # user_input 
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = user_input,
            max_tokens = 256,
            #stop = ".",
            temperature = 0.5,
        )
        chatgpt_response = response["choices"][0]["text"]
        request.session['chatgpt_response2'] = chatgpt_response

def editQuestion(request):
    print()
    obj = models.Question.objects.get(id=request.POST.get('editbtn'))
    obj.question = request.POST.get('edit')
    obj.save()

def deleteAllQuestios(value):
    models.Question.objects.filter(categoryId=value).delete()

def deleteCategory(value):
    models.Category.objects.filter(id=value).delete()

