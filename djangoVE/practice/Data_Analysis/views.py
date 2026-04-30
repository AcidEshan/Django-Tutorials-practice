from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def data_analysis(request):
    return HttpResponse('Hello, Data Analysis!')

def ai_engineering(request):
    return HttpResponse('Hello, AI Engineering!')
