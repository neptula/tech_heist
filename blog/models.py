from django.db import models

# Create your models here.
class blogDb(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True, null = True, blank = True)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    def __str__(self):
        return 'Blog written by ' + self.author


from blogger.utils import unique_slug_generator
from django.db.models.signals import pre_save
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender = blogDb)