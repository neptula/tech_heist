from django.shortcuts import render

# Create your views here.
from blog.models import blogDb

def writeblog(request):
  return render(request, 'writeBlog.html')


def showblog(request, slug=None):
  blog = blogDb.objects.get(slug = slug)
  context={
    'blog':blog
  }
  return render(request, 'showBlog.html', context)
