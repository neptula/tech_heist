from django.shortcuts import render

# Create your views here.
from blog.models import blogDb

def writeblog(request):
  return render(request, 'writeBlog.html')
