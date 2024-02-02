from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse('This is about page')
def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')
def loginform(request):
    mydist = {
        "Name":request.POST['username'],
        "Password":request.POST['password'],
        "Method":request.method
    }

    return JsonResponse(mydist)
