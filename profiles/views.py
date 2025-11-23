from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class CreateProfileView(View):
    def get(self,request:HttpRequest):
        return render(request, 'profiles/create-profile.html')
    def post(self , request:HttpRequest) :
        pass
