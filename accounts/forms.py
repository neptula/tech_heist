from django.contrib.auth import get_user_model
from django.contrib.auth import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models.base import Model
from accounts.models import userTags

class editprofileform(ModelForm):
    class Meta:
        model=User
        fields=("first_name","last_name", "email")
        labels={
                'first_name':'First name',
                'last_name':'last name',
                'email':'email',
        }
class extraFieldsProfileEditform(ModelForm):
    class Meta:
        model = userTags
        fields=('status','profile_image')
        labels={'status':'status',
        'profile_image':'Profile Image',
        }