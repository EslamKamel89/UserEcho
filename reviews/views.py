from typing import Optional

from django.http import (HttpRequest, HttpResponse,  # type: ignore
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from reviews.models import Review  # type: ignore

from .forms import ReviewForm


class ReviewView(View):
    def get(self , request:HttpRequest):
        form = ReviewForm()
        return render(request , 'reviews/index.html' , {'form' :form})

    def post(self , request:HttpRequest):
        form = ReviewForm(request.POST)
        if form.is_valid() :
            form.save()
            user_name:Optional[str] = form.cleaned_data['user_name']
            path = reverse('thank-you')
            return HttpResponseRedirect(f"{path}?username={user_name}")
        return render(request  , 'reviews/index.html' , {'form':form})

# def home(request:HttpRequest)->HttpResponse:
#     if request.method == 'POST' :
#         form = ReviewForm(request.POST)
#         if form.is_valid() :
#             form.save()
#             user_name:Optional[str] = form.cleaned_data['user_name']
#             path = reverse('thank-you')
#             return HttpResponseRedirect(f"{path}?username={user_name}")
#     else:
#         form = ReviewForm()
#     return render(request , 'reviews/index.html' , {"form" : form})

def thank_you(request:HttpRequest)->HttpResponse :
    username:Optional[str] = request.GET.get('username' , 'Guest')
    return render(request , 'reviews/thank-you.html' , {'username' :username})
