from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
# Create your views here.
from blog.models import blogDb, blogComment
from blog.templatetags import extras
from blog.forms import writeBlogForm
from accounts.models import userTags

def editblog(request, slug=None):
  blog = blogDb.objects.get(slug = slug)
  initVal = {
    'title': blog.title,
    'content': blog.content,
    'thumbnail':blog.thumbnail,
  }
  form = writeBlogForm(initial=initVal)
  params={ 'form':form, 'slug':slug }
  if request.method == 'POST':
    titlepost = request.POST.get('title')
    contentpost = request.POST.get('content')
    tagspost = request.POST.get('tags')
    # Handling Change of thumbnail
    if 'thumbnail' in request.FILES:
      thumbnailpost = request.FILES['thumbnail']
      blog.thumbnail = thumbnailpost
    blog.title = titlepost
    blog.content = contentpost
    blog.tags = tagspost
    blog.save()
    blog = blogDb.objects.get(title = titlepost)
    return redirect(f"/blog/showblog/{blog.slug}")
  else:
    
    return render(request, 'editblog.html', context=params)

def writeblog(request):

  if request.method =='POST':
    title=request.POST.get('title')
    author=request.POST.get('author')
    content=request.POST.get('content')
    tags = request.POST.get('tags')
    getthumbnail = request.FILES['thumbnail']
    tagsArr=tags.split(' ')
    initVal = {'title':title, 'content':content}
    form = writeBlogForm(request.POST, request.FILES, initial = initVal)
    # some checks of form

    if blogDb.objects.filter(title=title).exists():
      # messages.error(request,'Choose Unique Title')
      params={'title':title, 'author':author,'content':content,'tagsArr':tagsArr,'form':form}
      messages.warning(request, ' Choose Unique Title')
      return render(request, 'writeBlog.html', context = params)

    else:
      newBlog=blogDb(title=title, author=author, content=content, tags=tags, thumbnail=getthumbnail)
      newBlog.save()
      blog=blogDb.objects.get(title=title)
      return redirect(f"/blog/showblog/{blog.slug}")
  else:
    form = writeBlogForm()
    params={'title':"", 'author':"",'content':"", 'form':form}
    return render(request, 'writeBlog.html', context = params)



def showblog(request, slug=None):
  blog = blogDb.objects.get(slug = slug)
  comments = blogComment.objects.filter(blog=blog, parent=None)
  replies = blogComment.objects.filter(blog=blog).exclude(parent=None)
  blog.views = blog.views +1 
  blog.save();
  # Here I will create Dictionary for replies
  replyDict = {}
  for reply in replies:
    if reply.parent.sno not in replyDict.keys():
      replyDict[reply.parent.sno]=[reply]
    else:
      replyDict[reply.parent.sno].append(reply)


  tags = blog.tags
  tagsArr=tags.split(' ')

  context={
    'blog':blog, 'comments':comments, 'replyDict':replyDict, 'tagsArr':tagsArr
  }
  return render(request, 'showBlog.html', context)





def postComment(request):
  if request.method =='POST':
    comment = request.POST.get('comment')
    user = request.user
    uname = user.username
    blogSno = request.POST.get('blogSno')
    blog = blogDb.objects.get(sno=blogSno)
    # usertags = userTags.objects.get(username=user.username)
    # if usertags.profile_image:
    #   userImageUrl = usertags.profile_image.url
    # else :
    #   userImageUrl = "/static/images/defaultProfile.png"
    usertags = userTags.objects.get(username=uname) 
    parentSno = request.POST.get('parentSno')
    if parentSno=="":
      comment = blogComment(comment=comment, user=user, blog=blog,usertags=usertags)
      comment.save()
      messages.success(request, ' Your Comment posted Successfully')
    else:
      parent = blogComment.objects.get(sno=parentSno)
      comment = blogComment(comment=comment, user=user, blog=blog, parent=parent,usertags=usertags)

      comment.save()
      messages.success(request, ' Your Reply To Comment Posted Succeefully')

  return redirect(f"/blog/showblog/{blog.slug}")

class AddLike(LoginRequiredMixin, View):
    def post(self, request,slug, *args, **kwargs):
        post = blogDb.objects.get(slug=slug)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        post = blogDb.objects.get(slug=slug)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)