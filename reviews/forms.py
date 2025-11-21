from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator

from reviews.models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         widget=forms.TextInput(
#            attrs= {
#                 "class":"bg-gray-50 border rounded-lg text-heading text-sm focus:ring-brand focus:border-brand block w-full px-2.5 py-2 shadow-xs placeholder:text-body" ,
#                 "placeholder" : "Enter your name"
#             },
#         ) ,
#         max_length=100 , min_length=5 , label='Name' , error_messages={
#         "required":"Your name must not be empty" ,
#         "max_length" : "Please enter a shorter name!" ,
#         "min_length" :"please enter a longer name!"
#     })
#     content = forms.CharField(widget=forms.Textarea(
#          attrs= {
#                 "class":"bg-gray-50 border rounded-lg text-heading text-sm focus:ring-brand focus:border-brand block w-full px-2.5 py-2 shadow-xs placeholder:text-body" ,
#                 "placeholder" : "Comment"
#             }
#         ) , validators=[MinLengthValidator(10) , MaxLengthValidator(255)] , required=False)
#     rating = forms.IntegerField(min_value=1 , max_value=5 ,widget=forms.NumberInput(attrs= {
#                 "class":"bg-gray-50 border rounded-lg text-heading text-sm focus:ring-brand focus:border-brand block w-full px-2.5 py-2 shadow-xs placeholder:text-body" ,
#             }))
BASE_INPUT_CLASS = "bg-gray-50 border rounded-lg text-heading text-sm focus:ring-brand focus:border-brand block w-full px-2.5 py-2 shadow-xs placeholder:text-body"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields=['user_name' , 'content' , 'rating']
        fields = "__all__"
        labels = {
            'user_name':'Your Name' ,
            'content':'Your Comment' ,
            'rating':'Your Rating'
        }
        errors = {
            "user_name" : {
                "required":"Your name must not be empty" ,
                "max_length" : "Please enter a shorter name!" ,
                "min_length" :"please enter a longer name!"
            }
        }
        widgets = { # type: ignore
            "user_name": forms.TextInput(attrs={"placeholder": "Enter your name", "class": BASE_INPUT_CLASS}),
            "content": forms.Textarea(attrs={"placeholder": "Comment", "class": BASE_INPUT_CLASS}),
            "rating": forms.NumberInput(attrs={"class": BASE_INPUT_CLASS}),

        }

