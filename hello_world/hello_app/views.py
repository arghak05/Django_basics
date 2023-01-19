from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	text = "<h1>This is my first django app.</h1>"
	return HttpResponse(text)

