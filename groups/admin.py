from django.contrib import admin

# Register your models here.
from groups.models import Group, GroupMember

admin.site.register((Group, GroupMember))
