from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.getArticles, name='articulos'),
    path('categoria/<int:categoryID>', views.getCategory, name='categoria'),
]
