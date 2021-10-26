from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from blog.models import blogDb, blogComment
from blog.templatetags import extras

def writeblog(request):
  if request.method =='POST':
    title=request.POST.get('title')
    author=request.POST.get('author')
    content=request.POST.get('content')
    # some checks of form

    if blogDb.objects.filter(title=title).exists():
      # messages.error(request,'Choose Unique Title')
      params={'title':title, 'author':author,'content':content}
      messages.warning(request, ' Choose Unique Title')
      return render(request, 'writeBlog.html', params)






    else:
      newBlog=blogDb(title=title, author=author, content=content)
      newBlog.save()
      blog=blogDb.objects.get(title=title)
      return redirect(f"/blog/showblog/{blog.slug}")
  else:
    params={'title':"", 'author':"",'content':""}
    return render(request, 'writeBlog.html')



def showblog(request, slug=None):
  blog = blogDb.objects.get(slug = slug)
  comments = blogComment.objects.filter(blog=blog, parent=None)
  replies = blogComment.objects.filter(blog=blog).exclude(parent=None)

  # Here I will create Dictionary for replies
  replyDict = {}
  for reply in replies:
    if reply.parent.sno not in replyDict.keys():
      replyDict[reply.parent.sno]=[reply]
    else:
      replyDict[reply.parent.sno].append(reply)



  context={
    'blog':blog, 'comments':comments, 'replyDict':replyDict
  }
  return render(request, 'showBlog.html', context)





def postComment(request):
  if request.method =='POST':
    comment = request.POST.get('comment')
    user = request.user
    blogSno = request.POST.get('blogSno')
    blog = blogDb.objects.get(sno=blogSno)
    parentSno = request.POST.get('parentSno')
    if parentSno=="":
      comment = blogComment(comment=comment, user=user, blog=blog)
      comment.save()
      messages.success(request, ' Your Comment posted Successfully')
    else:
      parent = blogComment.objects.get(sno=parentSno)
      comment = blogComment(comment=comment, user=user, blog=blog, parent=parent)

      comment.save()
      messages.success(request, ' Your Reply To Comment Posted Succeefully')

  return redirect(f"/blog/showblog/{blog.slug}")
