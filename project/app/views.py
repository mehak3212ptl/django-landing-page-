from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return redirect("https://github.com/mehak3212ptl")

def home(request):
    return HttpResponse("this is my app11111111111111111111111")