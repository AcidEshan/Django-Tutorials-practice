from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machine_learning(request):
    return HttpResponse('<h1>I am starting my machine learning journey!</h1>')

def deep_learning(request):
    return HttpResponse('<h1>I am starting my deep learning journey!</h1>')

def about_us(request):
    return HttpResponse('<h1>About Us</h1><p>Welcome to our machine learning and deep learning course!</p>')
