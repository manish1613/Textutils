

# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index1.html')

    # return HttpResponse("Home")



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyzer.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyzer.html', params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if(char!="\n" and char!="\r"):
                analyzed = analyzed + char

        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyzer.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if (djtext[index]==" " and djtext[index+1]==" "):
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}



    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Please Choose any option")
    return render(request, 'analyzer.html', params)

