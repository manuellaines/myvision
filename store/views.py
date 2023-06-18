# from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    messages='hello'
    return HttpResponse(messages)
# Create your views here.
