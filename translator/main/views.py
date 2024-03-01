from django.shortcuts import render,HttpResponse
from translate import Translator

# Create your views here.
def get_translation(request):
    if request.method == 'POST':
        text = request.POST['text']
        language = request.POST['language']
        translator = Translator(to_lang=language)
        translation = translator.translate(text)
        return HttpResponse(translation)


    return render(request,'main/index.html')
