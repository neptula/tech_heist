from django.contrib import admin

# Register your models here.
from blog.models import blogDb, blogComment

admin.site.register((blogDb, blogComment))



