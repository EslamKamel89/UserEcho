
from django.urls import URLPattern, path

from . import views

urlpatterns:list[URLPattern] = [
    path('' , views.home ),
    path('thank-you' , views.thank_you , name='thank-you')
]
