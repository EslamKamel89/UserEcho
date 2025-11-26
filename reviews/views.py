from typing import Any

from django.http import HttpRequest
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from reviews.models import Review  # type: ignore

from .forms import ReviewForm


class ReviewView(CreateView):
    form_class = ReviewForm
    model = Review
    template_name = 'reviews/index.html'
    success_url = 'thank-you'



class ThankYouView(TemplateView):
    template_name = 'reviews/thank-you.html'
    def get_context_data(self , **kwargs:Any)->dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['message'] = 'Thank you for submitting you review'
        return context

class ReviewsListView(ListView) :
    template_name = 'reviews/review-list.html'
    model = Review
    context_object_name = 'reviews'
    def get_queryset(self):
        query =  super().get_queryset()
        query = query.filter(rating__gt=0)
        return query



class SingleReviewView(DetailView):
    template_name = "reviews/single-review.html"
    model = Review

class AddFavoriteView(View):
    def post(self , request:HttpRequest):
        review_id = int(request.POST.get('review_id' , '0'))
        fav_review = Review.objects.get(pk=review_id)

