from django.shortcuts import render
import pyjokes
# Create your views here.
def joke_generator(request):
    joke = pyjokes.get_joke(language='en')
    return render(request,'main/index.html',{'joke':joke})

    