from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, Index Page')

def about(request):
    return HttpResponse('About Page')

def contact(request):
    return HttpResponse('Contact Page')

def persons(request):
    return HttpResponse('Persons Page')