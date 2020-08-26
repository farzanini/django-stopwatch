from django.shortcuts import render


def showHomePage(request):
    if request.method == "POST":
        pass
    return render(request, 'sampleApp/index.html')
# Create your views here.
