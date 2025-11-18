from django.http import HttpRequest, HttpResponse, JsonResponse  # type: ignore
from django.shortcuts import render  # type: ignore

# Create your views here.

def test(request:HttpRequest)->JsonResponse:
    return JsonResponse({'message':"👋 welcome"})