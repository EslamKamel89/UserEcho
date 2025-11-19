from typing import Optional

from django.http import (HttpRequest, HttpResponse,  # type: ignore
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import render
from django.urls import reverse  # type: ignore

# Create your views here.

def home(request:HttpRequest)->HttpResponse:
    if request.method == 'POST':
        username:Optional[str] = request.POST.get('username' , 'Guest')
        path = reverse('thank-you')
        return HttpResponseRedirect(f"{path}?username={username}")
    return render(request , 'reviews/index.html')

def thank_you(request:HttpRequest)->HttpResponse :
    username:Optional[str] = request.GET.get('username' , 'Guest')
    return render(request , 'reviews/thank-you.html' , {'username' :username})
