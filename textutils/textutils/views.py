# I have created this file naval kshor

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('''About naval <a href='/'>Back</a>''')


def analyze(request):
    # receive text area value from form
    dtext = request.POST.get('text', 'default')

    # checking checkbox value is on or off
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    # punctuation list
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepunc == "on":
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        prams = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        dtext = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in dtext:
            analyzed = analyzed + char.upper()
        prams = {'purpose': 'Change to Upper case', 'analyzed_text': analyzed}
        dtext = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in dtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        prams = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on":
        return HttpResponse("Please Choose one of the Action")
    else:
        return render(request, 'analyze.html', prams)

