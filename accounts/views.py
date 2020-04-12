from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home page')

def products(request):
    return HttpResponse('contact page')

def customer(request):
    return HttpResponse('contact page')    
# Create your views here.
