from django.shortcuts import render
import openai,os
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("OPENAI_KEY",None)
openai.api_key = api_key 



def chatGPT(request):
    #user_input = "what is a doberman?"
    print("test")
    chatgpt_response = None
    if api_key is not None and request.method == 'POST':
        #openai.api_key = api_key
        user_input = request.POST.get('user_input') # user_input 
        #prompt = user_input
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = user_input,
            max_tokens = 256,
            #stop = ".",
            temperature = 0.5,
        )
        #print(response)
        chatgpt_response = response["choices"][0]["text"]
    return render(request,'chatGPT/main.html',{"response":chatgpt_response})







