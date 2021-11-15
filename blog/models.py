from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from accounts.models import userTags

# Create your models here.
class blogDb(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique = True)
    author = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True, null = True, blank = True)
    content = RichTextField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tags = models.CharField(max_length=255)
    blogpriority = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to="static/images/%y")
    # content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    likes=models.ManyToManyField(User,related_name='blikes',blank=True)
    dislikes=models.ManyToManyField(User,related_name='bdislikes',blank=True)
    def __str__(self):
        return 'Blog written by ' + self.author
    


from blogger.utils import unique_slug_generator
from django.db.models.signals import pre_save
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender = blogDb)




class blogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usertags = models.ForeignKey(userTags, on_delete=models.CASCADE)
    blog = models.ForeignKey(blogDb, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)