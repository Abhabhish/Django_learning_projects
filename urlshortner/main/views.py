from django.shortcuts import render
import requests

# Create your views here.
def short_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('longurl')
        headers = {
                'Authorization': 'Bearer 117a565b45a474b477773738561abd54b8513149',
            }
        data = f'{{ "long_url": "{long_url}" }}'
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
        short_url = response.json()['link']
        return render(request,'main/index.html',{'short_url':short_url})
    return render(request,'main/index.html')


