from django.urls import path

# Import django's auth views
from django.contrib.auth import views as auth_views

# Import local views.py file
from . import views

urlpatterns = [
    path('', views.loginView, name = 'login'),
    path('registration/', views.registerView, name = 'registration'),
    path('logout/', views.logoutView, name = 'logout'),
    path('fill_details/', views.fillDetailsView, name = 'fill_details'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'reset_request.html'),
    name = "password_reset"),

    path('reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'reset_mail_sent.html'),
    name = "password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'reset_password.html'),
    name = "password_reset_confirm"),

    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'reset_confirm.html'),
    name = "password_reset_complete"),
]

