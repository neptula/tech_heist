from django.contrib.auth import get_user_model
from django.contrib.auth import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models.base import Model

class editprofileform(UserChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    #date_joined=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    #is_superuser=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    #is_staff=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    #last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=get_user_model()
        fields=("username","first_name","last_name", "email","is_active")

# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
# from django import forms

# class SignUpForm(UserCreationForm):
#     extra_field=forms.CharField(required=True)


#     class Meta:
#         model = get_user_model()
#         fields = ("username", "email", "password1", "password2","extra_field", 'image')
#         widgets={
#             'image': forms.CharField(max_length=255)
#         }
    


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["username"].label = "Display name"
#         self.fields["email"].label = "Email address"
#         self.fields["extra_field"].label = "Interested Topics"

        
