from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
from . import forms

class SignUp(CreateView):
  form_class=forms.SignUpForm
  success_url=reverse_lazy('login')
  template_name='accounts/signup.html'