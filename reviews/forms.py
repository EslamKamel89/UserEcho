from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=100 , min_length=5 , label='Name' , error_messages={
        "required":"Your name must not be empty" ,
        "max_length" : "Please enter a shorter name!" ,
        "min_length" :"please enter a longer name!"
    })
