from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar_producto, name='buscar_producto'),
    path('contador/', views.consulta_producto_view, name='consulta_producto_view'),
]

# urls.py


