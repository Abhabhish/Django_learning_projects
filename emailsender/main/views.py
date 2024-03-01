from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        subject = 'Welcom This is Abhishek'
        message = 'Aur bhai '+name+' kya haal hai?'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
        

    return render(request,'main/index.html')