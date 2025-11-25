from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from profiles.forms import ProfileForm
from profiles.models import UserProfile


def store_file(uploaded_file:UploadedFile):
    print(uploaded_file)
    with open('temp/image.png' , 'wb+') as dest:
        for chunk in uploaded_file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self,request:HttpRequest):
        form = ProfileForm()
        return render(request, 'profiles/create-profile.html' , {"form":form})
    def post(self , request:HttpRequest) :
        form = ProfileForm(request.POST , request.FILES)
        file = request.FILES.get('user_image')
        if form.is_valid() and file:
            # store_file(file)
            profile = UserProfile(image=file)
            profile.save()
            return HttpResponseRedirect('/profiles' ,)
        return render(request, 'profiles/create-profile.html' , {"form":form})

