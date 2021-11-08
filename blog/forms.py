from blog.models import blogDb
from django.forms import ModelForm


class writeBlogForm(ModelForm):
    class Meta:
        model = blogDb
        fields = ['title',  'content', 'thumbnail']
        labels = {'title':'Enter Title of Your Blog', 'content':'Write Content Of your Blog Here                                                            ', 'thumbnail':'Add thumbnail for your Blog'}        