from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView
from translate import Translator


def translationview(request):
    if request.method == "POST":
        lan_src = request.POST["lan_src"]
        lan_den = request.POST["lan_den"]
        txt_src = request.POST["txt_src"]
        translator = Translator(from_lang=lan_src, to_lang=lan_den)
        translation = translator.translate(txt_src)
        return render(request, 'index.html', {"txt_den": translation, "txt_src": txt_src})
    return render(request, 'index.html')
