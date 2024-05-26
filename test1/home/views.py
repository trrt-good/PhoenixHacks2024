from django.shortcuts import render

# Create your views here.

def callPage(request):
    return render(request, 'hello.html')