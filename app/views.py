from django.shortcuts import render

# Create your views here.

def webpage(request):
    return render(request,'index.html')