from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def myfunctioncall(request):
    return HttpResponse("Starting to learn Django")

def about(request):
    return HttpResponse('This is about page')