from typing import Any, Optional

from django.http import (HttpRequest, HttpResponse,  # type: ignore
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView

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


class ThankYouView(TemplateView):
    template_name = 'reviews/thank-you.html'
    def get_context_data(self , **kwargs:Any)->dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['message'] = 'Thank you for submitting you review'
        return context

class ReviewsListView(ListView) :
    template_name = 'reviews/review-list.html'
    model = Review


class SingleReviewView(TemplateView):
    template_name = "reviews/single-review.html"
    def get_context_data(self ,**kwargs:Any)->dict[str, Any]:
        context = super().get_context_data(**kwargs)
        review = get_object_or_404(Review ,id= kwargs['id'])
        context['review'] = review
        return context
