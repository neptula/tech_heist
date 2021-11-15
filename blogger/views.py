from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User 
from blog.models import blogDb
from accounts.models import userTags

def index(request):
    allBlogs=blogDb.objects.all()
    if allBlogs.count() > 10:
        last_ten = blogDb.objects.all().order_by('-sno')[:10]
        context = {'allBlogs':last_ten}
    else:
        allBlogs = blogDb.objects.all().order_by('-sno')
        context = {'allBlogs':allBlogs}
    return render(request, 'index.html', context)


def search(request):
    query = request.GET['query']
    allBlogsTitle = blogDb.objects.filter(title__icontains=query)
    allBlogsTags = blogDb.objects.filter(tags__icontains=query)
    if allBlogsTitle.count()== 0 and allBlogsTags.count()==0:
        messages.warning(request, 'No Search Results Found Please refine Your Query')
    params = {'allBlogsTitle':allBlogsTitle, 'allBlogsTags':allBlogsTags ,'query':query}
    return render(request, 'searchResults.html', params)


def blogs(request):
    # In this page our goal is to show blogs with priority
    allBlogs = blogDb.objects.all()
    username = request.user.get_username()
    # print(username)

    myuser=userTags.objects.get(username=username)
    myuserinterests=myuser.interestingTags
    userinterestsArr=myuserinterests.split(' ')
    for blog in allBlogs:
        blog.blogpriority = 0
        blog.save()
    for blog in allBlogs:
        blogtags=blog.tags
        blogtagsArr=blogtags.split(' ')
        # print(blogtagsArr)
        for interest in userinterestsArr:
            if interest:    
                for tag in blogtagsArr:
                    if interest == tag:
                        blog.blogpriority=blog.blogpriority+1
                        blog.save()


    allBlogs = blogDb.objects.all()
    context = {'allBlogs':allBlogs}
    return render(request, 'blogs.html', context)