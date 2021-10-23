from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
from django.contrib import messages



from blog.models import blogDb

def index(request):
    allBlogs = blogDb.objects.all()
    context = {'allBlogs':allBlogs}
    return render(request, 'index.html', context)


def search(request):
    query = request.GET['query']
    allBlogs = blogDb.objects.filter(title__icontains=query)
    if allBlogs.count()== 0:
        messages.warning(request, 'No Search Results Found Please refine Your Query')
    params = {'allBlogs':allBlogs, 'query':query}
    return render(request, 'searchResults.html', params)