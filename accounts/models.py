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


