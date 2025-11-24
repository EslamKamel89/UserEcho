from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class CreateProfileView(View):
    def get(self,request:HttpRequest):
        return render(request, 'profiles/create-profile.html')
    def post(self , request:HttpRequest) :
        print({"image":request.FILES.get('image') , "username":request.POST.get('username')})
        return HttpResponseRedirect('/profiles')

