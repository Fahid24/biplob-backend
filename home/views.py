from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products

class ProductsListCreateView(generics.ListCreateAPIView):
    queryset = Products.objects.all()  # Fix the typo here
    serializer_class = ProductsSerializer
    
class ProductsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()  # Fix the typo here
    serializer_class = ProductsSerializer
    
def home(request):
    return HttpResponse("hi fuad server is on")


@api_view(['POST'])
def upload_product(request):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
