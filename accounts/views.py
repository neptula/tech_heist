# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
from . import forms
from .forms import editprofileform,extraFieldsProfileEditform
from accounts.models import contact
from accounts.models import userTags
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 
from blog.models import blogDb

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
        messages.warning(request, " Passwords do not match ☺")
        return redirect('accounts:signup')

      
      # Create the user
      myuser = User.objects.create_user(username, email, pass1)
      myuser.save()
      newusertags = userTags(username=username, interestingTags=interestingTags) 
      newusertags.save()
      messages.success(request, " Your account has been created successfully !!!")
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

class passwordchangedview(PasswordChangeView):
  form_class=PasswordChangeForm  
  success_url=reverse_lazy('accounts:show_profile')


# class UserEditView(UpdateView):
#   form_class=editprofileform
#   success_url=reverse_lazy('index')
#   template_name='accounts/profile_user.html'

#   def get_object(self):
#       return self.request.user

# class displayprofile(TemplateView):
  
#   template_name='accounts/display_profile.html'
def UserEditView(request):
  initval1={
    'first_name':request.user.first_name,
    'last_name':request.user.last_name,
    'email':request.user.email,
  }
  form=editprofileform(initial=initval1)
  usertags=userTags.objects.get(username=request.user.username)
  interests=usertags.interestingTags
  initval2={
    'status':usertags.status,
    'profile_image':usertags.profile_image,
  }
  form2=extraFieldsProfileEditform(initial=initval2)
  username=request.user
  if request.method=='POST':
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email=request.POST.get('email')
    interestingTags=request.POST['tags']
    status=request.POST.get('status')
    if request.FILES:
      image=request.FILES['profile_image']
      usertags=userTags.objects.get(username=username)
      usertags.profile_image=image
      usertags.save()
    # print(first_name, last_name, email, status)
    user=User.objects.get(username=username)
    user.first_name=first_name
    user.last_name=last_name
    user.email=email
    user.save()

    usertags=userTags.objects.get(username=username)
    usertags.status=status
    usertags.interestingTags=interestingTags
    usertags.save()
    messages.success(request, 'Profile Updated Successfully')
    return redirect('accounts:show_profile')
  dictn={'form':form, 'username':username, 'form2':form2, 'interests':interests}
  return render(request, 'accounts/profile_user.html', context=dictn)

def displayprofile(request):
  username=request.user
  usertags=userTags.objects.get(username=username)
  context={'usertags':usertags}
  return render(request, 'accounts/display_profile.html', context)


def filterByUsername(request):
  query = request.user.username
  allBlogs = blogDb.objects.filter(author=query)
  if allBlogs.count()== 0:
    messages.warning(request, " You haven't written any blog yet !!!")
  params = {'allBlogs':allBlogs}
  return render(request,'accounts/filterByUsername.html', params)
