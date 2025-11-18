from django.http import HttpRequest, HttpResponse, JsonResponse  # type: ignore
from django.shortcuts import render  # type: ignore

# Create your views here.

def home(request:HttpRequest)->HttpResponse:
    return render(request , 'reviews/index.html')