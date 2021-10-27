from blog.models import blogDb
from django.forms import ModelForm


class writeBlogForm(ModelForm):
    class Meta:
        model = blogDb
        fields = ['title',  'content']
        labels = {'title':'Enter Title of Your Blog', 'content':'Write Content Of your Blog Here                                                            '}        