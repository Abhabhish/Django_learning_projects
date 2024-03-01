from django.shortcuts import render
import wikipedia

# Create your views here.

def wikisearch(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        print(topic)
        try:
           topic_summary = wikipedia.summary(topic,sentences = 5)
        except:
            topic_summary = 'Wrong Input'
        return render(request,'main/index.html',{'summary':topic_summary})
    return render(request,'main/index.html')
