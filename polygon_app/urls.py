from django.urls import path
from .views import connect_polygon_network

urlpatterns = [
    path('connect/', connect_polygon_network, name='connect_polygon_network'),
]