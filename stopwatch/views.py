from django.shortcuts import render


def showHomePage(request):
    if request.method == "POST":
        pass
    return render(request, 'stopwatch/index.html')
# Create your views here.
