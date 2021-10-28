from django.conf.urls import url
from django.urls import include, path, re_path

from . import views

app_name='posts'

urlpatterns = [
    re_path(r"^$", views.PostList.as_view(), name="all"),
    re_path(r"new/$", views.CreatePost.as_view(), name="create"),
    re_path(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    re_path(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"),
    re_path(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
    path('posts/<int:pk>/likes/',views.AddLike.as_view(),name='like'),
    path('posts/<int:pk>/dislikes/',views.AddDislike.as_view(),name='dislike'),
]
