from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views

app_name = 'blog'

urlpatterns = [
    path('writeblog/', views.writeblog,name='writeblog'),

]
