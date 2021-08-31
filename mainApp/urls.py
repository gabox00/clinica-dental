from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.index, name='index'),
    path('registro/', views.registerUser, name='registro'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout')
]
