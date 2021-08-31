from django.urls import path
from . import views

urlpatterns = [
    path('pagina/<str:slug>', views.getPage, name='page'),
    path('agregar-cita/', views.crudCita, name='crudCita'),
    path('procesar-cita/', views.processCita, name='processCita')
]
