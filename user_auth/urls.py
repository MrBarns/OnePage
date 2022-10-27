from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginView, name = 'login'),
    path('registration/', views.registerView, name = 'registration'),
    path('logout/', views.logoutView, name = 'logout'),
    path('fill_details/', views.fillDetailsView, name = 'fill_details'),
]