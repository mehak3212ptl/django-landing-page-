from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is my app2")

def login (request):
    return HttpResponse("this is my login page of app2")