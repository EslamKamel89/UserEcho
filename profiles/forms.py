from django import forms


class ProfileForm(forms.Form):
    # username = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={"class":"bg-gray-50 border rounded-lg text-heading text-sm focus:ring-brand focus:border-brand block w-full px-2.5 py-2 shadow-xs placeholder:text-body"}
    #         ),
    #     error_messages={
    #         "required":"Your name must not be empty" ,
    #         }
    #     )
    user_image = forms.ImageField(
        required=True ,
        widget= forms.FileInput(
            attrs={"class":"block w-full text-sm text-gray-700 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-sm file:font-medium file:bg-blue-600 file:text-white hover:file:bg-blue-700 cursor-pointer"}

            ),
        error_messages={
            "required":"Your must upload your profile image" ,
            }
        )
