from django.db import models

# Create your models here.
class blogDb(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 200)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    def __str__(self):
        return 'Blog written by ' + self.author


