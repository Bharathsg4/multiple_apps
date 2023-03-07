from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app1(request):
    return HttpResponse('<h1>This is first function of app1</h1>')

def second_app1(request):
    return HttpResponse('<h1>This is second function of app1</h1>')