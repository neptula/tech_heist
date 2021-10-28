from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.conf import settings
from django.urls import reverse

from groups.models import  Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = RichTextField(blank=True, null=True)
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    dislikes=models.ManyToManyField(User,related_name='dislikes',blank=True)

    def _str_(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = self.message
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )
   
    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]
