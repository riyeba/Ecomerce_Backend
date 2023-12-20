from django.shortcuts import render
from .models import Category,Product,Brand
from .serializers import CategorySerializer,ProductSerializer,BrandSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
# Create your views here.




@api_view(['GET', 'POST'])
@permission_classes([AllowAny,])
def Category_list(request, format=None):
      
    if request.method =='GET':
       category=Category.objects.all()
       serializer=CategorySerializer(category, many=True)
       return Response(serializer.data)
     
    if request.method=='POST':
       serializer=CategorySerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT','DELETE'])
def Category_detail(request,id,format=None):
    
    try:
       category= Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
       serializer= CategorySerializer(category)
       return Response(serializer.data)
        
    elif request.method=='PUT':
        serializer= CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
    elif request.method=='DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      
      

@api_view(['GET', 'POST'])
@permission_classes([AllowAny,])
def Product_list(request, format=None):
      
    if request.method =='GET':
       product=Product.objects.all()
       serializer=ProductSerializer(product, many=True)
       return Response(serializer.data)
     
    if request.method=='POST':
       serializer=ProductSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
     
   
@api_view(['GET', 'PUT','DELETE'])
def Product_detail(request,id,format=None):
    
    try:
       product= Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
       serializer= ProductSerializer(product)
       return Response(serializer.data)
        
    elif request.method=='PUT':
        serializer= ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
    elif request.method=='DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   



@api_view(['GET', 'POST'])
@permission_classes([AllowAny,])
def Brand_list(request, format=None):
      
    if request.method =='GET':
       brand=Brand.objects.all()
       serializer=BrandSerializer(brand, many=True)
       return Response(serializer.data)
     
    if request.method=='POST':
       serializer=BrandSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
     
   
@api_view(['GET', 'PUT','DELETE'])
def Brand_detail(request,id,format=None):
    
    try:
       brand= Brand.objects.get(pk=id)
    except Brand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
       serializer= BrandSerializer(brand)
       return Response(serializer.data)
        
    elif request.method=='PUT':
        serializer= BrandSerializer(brand,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
    elif request.method=='DELETE':
        
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   



           


      
   
   

    



     
    
     
   

    
   
        
   
   


     
   
     
   

    
        
    
   


      
     
   

    
      
        
    
   

