from django.views.generic import TemplateView
from django.shortcuts import render


from blog.models import blogDb

def index(request):
    allBlogs = blogDb.objects.all()
    context = {'allBlogs':allBlogs}
    return render(request, 'index.html', context)


