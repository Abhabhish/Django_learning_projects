from django.shortcuts import render,HttpResponse
from .forms import ContactForm
# Create your views here.

def contact(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            return HttpResponse('You Proved You are Human')
        else:
            return HttpResponse('You are a Robot')

    fm = ContactForm()
    return render(request,'contact.html',{'form':fm})