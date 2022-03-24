from functools import partial
from urllib import response
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import productserializer
from .models import Product
from rest_framework import status

# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def product_api(request,pk=None):
    if request.method ==  'GET':
        id = pk
        if id is not None:
            prod = Product.objects.get(id=id)
            serilizer = productserializer(prod)
            return Response(serilizer.data)
        prod = Product.objects.all()
        serilizer = productserializer(prod,many=True)
        return Response(serilizer.data)

    if request.method == 'POST':
        serilizer = productserializer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = pk
        prod = Product.objects.get(pk=id)
        serilizer = productserializer(prod,data = request.data )
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)  

    if request.method == 'PATCH':
        id = pk
        prod = Product.objects.get(pk=id)
        serilizer = productserializer(prod,data = request.data,partial =True )
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)  



    if request.method == 'DELETE':
        id = pk
        prod = Product.objects.get(pk=id)
        prod.delete()
        return Response({})
    



