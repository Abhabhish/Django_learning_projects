from django.shortcuts import render,redirect
from .models import UserEmail

# Create your views here.

def sub_unsub(request):
    email_list = UserEmail.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        if 'Subscribe' in request.POST:
            user_email = UserEmail(email= email)
            user_email.save()
        else:
            UserEmail.objects.get(email=email).delete()
        # return render(request,'main/index.html',{'emails':email_list})
    return render(request,'main/index.html',{'emails':email_list})