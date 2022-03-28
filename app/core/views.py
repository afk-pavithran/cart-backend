from django.shortcuts import render
from django.http import HttpResponseGone

# Create your views here.
def index(request):
    return HttpResponseGone("Welocme to index")