# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
from . import forms
from accounts.models import contact
from accounts.models import userTags
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 

# class SignUp(CreateView):
#   form_class=forms.SignUpForm
#   success_url=reverse_lazy('login')
#   template_name='accounts/signup.html'


def SignUp(request):
    if request.method=="POST":
      # Get the post parameters
      username=request.POST['username']
      email=request.POST['email']
      pass1=request.POST['pass1']
      pass2=request.POST['pass2']
      interestingTags=request.POST['tags']

      # check for errorneous input
      if len(pass1)<8:
        messages.warning(request, " Your password must contain 8 characters")
        return redirect('accounts:signup')

      if not username.isalnum():
        messages.warning(request, " User name should only contain letters and numbers")
        return redirect('accounts:signup')

      if User.objects.filter(username=username).exists():
        # messages.error(request,'Choose Unique Title')
        messages.warning(request, ' Choose Unique username')
        return redirect('accounts:signup')


      if (pass1!= pass2):
        messages.warning(request, " Passwords do not match")
        return redirect('accounts:signup')

      
      # Create the user
      myuser = User.objects.create_user(username, email, pass1)
      myuser.save()
      newusertags = userTags(username=username, interestingTags=interestingTags) 
      newusertags.save()
      messages.success(request, " Your iCoder has been successfully created")
      return redirect('accounts:login')
    else:
      return render(request, 'accounts/signup.html')

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

