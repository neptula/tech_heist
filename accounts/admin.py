from django.contrib import admin
from accounts.models import contact
from accounts.models import userTags

# Register your models here.

admin.site.register((contact,userTags))