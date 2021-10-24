from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views

app_name = 'blog'

urlpatterns = [
    path('postComment', views.postComment, name='postComment'),
    path('writeblog/', views.writeblog,name='writeblog'),
    path('showblog/<str:slug>', views.showblog,name='showblog'),

]
