from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views

app_name = 'blog'

urlpatterns = [
    path('postComment', views.postComment, name='postComment'),
    path('writeblog/', views.writeblog,name='writeblog'),
    path('editblog/<str:slug>', views.editblog,name='editblog'),
    path('showblog/<str:slug>', views.showblog,name='showblog'),
    path('showblog/<str:slug>/likes/',views.AddLike.as_view(),name='like'),
    path('showblog/<str:slug>/dislikes/',views.AddDislike.as_view(),name='dislike'),

]
