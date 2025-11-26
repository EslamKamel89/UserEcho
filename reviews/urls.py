
from django.urls import URLPattern, path

from . import views

urlpatterns:list[URLPattern] = [
    path('' , views.ReviewView.as_view() ),
    path('thank-you' , views.ThankYouView.as_view() , name='thank-you'),
    path('reviews' , views.ReviewsListView.as_view()),
    path('reviews/favorite' , views.AddFavoriteView.as_view()),
    path('reviews/<int:pk>' , views.SingleReviewView.as_view())
]
