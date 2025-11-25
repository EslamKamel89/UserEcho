from django.core.files.uploadedfile import UploadedFile
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from profiles.forms import ProfileForm
from profiles.models import UserProfile


def store_file(uploaded_file:UploadedFile):
    print(uploaded_file)
    with open('temp/image.png' , 'wb+') as dest:
        for chunk in uploaded_file.chunks():
            dest.write(chunk)

class CreateProfileView(CreateView):
    model = UserProfile
    form_class = ProfileForm
    success_url = '/profiles'
    template_name = 'profiles/create-profile.html'


class ProfilesView(ListView):
    template_name="profiles/user-profiles.html"
    model=UserProfile
    context_object_name = "profiles"
