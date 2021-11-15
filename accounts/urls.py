from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserEditView,passwordchangedview,displayprofile

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp, name="signup"),
    path('contactus/', views.contactus,name='contactus'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),
    path('edit_profile/', views.UserEditView, name="edit_profile"),
    path('show_profile/', views.displayprofile, name="show_profile"),

   # path('password/',auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html')),
    path('password/',passwordchangedview.as_view(template_name='accounts/password_change.html'), name="password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),
    path('BlogsWrittenByYou/', views.filterByUsername,name='filterByUsername'),
    
]
