from django.urls import path
from .views import *





urlpatterns = [
    path('products/', ProductsListCreateView.as_view(), name='products list create'),
    path('products/<int:pk>', ProductsDetailView.as_view(), name='products list detail')
]
