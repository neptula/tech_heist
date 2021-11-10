from django.db import models

# Create your models here.
# Models is Django ----->Table is DataBase Or Sheet

class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contactNo = models.CharField(max_length = 13)
    email = models.CharField(max_length = 100)
    issue = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message From ' + self.name


class userTags(models.Model):
    username = models.CharField(max_length=255)
    interestingTags = models.CharField(max_length=255)
    status=models.TextField(max_length=255, null=True, blank=True)
    profile_image=models.ImageField(upload_to="static/images/%y")

    def __str__(self):
        return 'Interests of ' + self.username


