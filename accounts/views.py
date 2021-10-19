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

def contactus(request):
  if request.method == 'POST':
    name = request.POST['Username']
    email = request.POST['mailid']
    phoneNo = request.POST['phoneNo']
    issue = request.POST['issue']
    # print(name + email + phoneNo + issue)
    newcontact = contact(name=name, contactNo=phoneNo, email=email, issue=issue)
    newcontact.save()
    messages.success(request, 'We have received Your Mail we will contact You Soon')
  return render(request, 'accounts/contactus.html')

