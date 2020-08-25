from django.shortcuts import render


def showHomePage(request): 
    return render(request, 'sampleApp/index.html')
# Create your views here.
