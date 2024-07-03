from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menus/', views.menu, name='menu'),
    path('evento/', views.evento, name='evento'),
    path('contacto/', views.contacto, name='contacto'),
    # otras rutas que tengas
]
