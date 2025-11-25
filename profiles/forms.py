from tkinter import Widget

from django import forms

from profiles.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta :
        model = UserProfile
        fields = ['image']
        widgets = {
             'image': forms.FileInput(
                attrs={
                    "class":"block w-full text-sm text-gray-700 file:mr-4 file:py-2 "
                           "file:px-4 file:rounded-xl file:border-0 file:text-sm "
                           "file:font-medium file:bg-blue-600 file:text-white "
                           "hover:file:bg-blue-700 cursor-pointer"
                }
            )
        }
        error_messages = {
            'image': {
                'required': "You must upload your profile image",
            }
        }
