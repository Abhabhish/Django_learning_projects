from django.shortcuts import render, redirect
from .models import UrlSlug
from .forms import UrlForm
import random
import string


# Create your views here.
def url_shortner(request):
    if request.method == 'POST':
        fm = UrlForm(request.POST)
        
        if fm.is_valid():
            print('valid')
            url = fm.cleaned_data['url']
            slug = ''.join([random.choice(string.ascii_letters) for x in range(10)])
            url_slug = UrlSlug(url=url,slug=slug)
            url_slug.save()
            return redirect('url_shortner')

    fm = UrlForm()
    data = UrlSlug.objects.all()
    context = {'form':fm,'data':data}
    return render(request,'main/index.html',context)

def redirect_url(request,slug):
    url = UrlSlug.objects.get(slug=slug).url
    return redirect(url)