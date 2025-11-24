from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from profiles.forms import ProfileForm


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
        image = request.FILES.get('image')
        if image is not None:
            store_file(image)
        return HttpResponseRedirect('/profiles')

