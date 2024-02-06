from django.shortcuts import render
from .models import Category,Product,Brand,Cart
from .serializers import CategorySerializer,ProductSerializer,BrandSerializer,CartSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.http import Http404
# Create your views here.

from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters


class Product_list(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    # filterset_fields= ['title','category','brand']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'category__categoryname','brand__brandname']
    # ordering_fields = "__all__"
    
# class Category_list(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
   
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['categoryname']
#     # ordering_fields = "__all__"

class Category_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        carts =  Category.objects.all()
        serializer = CategorySerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Category_detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Cart_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        carts =  Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Cart_detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        carts = self.get_object(pk)
        serializer = CartSerializer(carts)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        carts = self.get_object(pk)
        serializer = CartSerializer(carts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        carts = self.get_object(pk)
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny,])
# def Category_list(request, format=None):
      
#     if request.method =='GET':
#        category=Category.objects.all()
#        serializer=CategorySerializer(category, many=True)
#        return Response(serializer.data)
     
#     if request.method=='POST':
#        serializer=CategorySerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# @api_view(['GET', 'PUT','DELETE'])
# def Category_detail(request,title,format=None):
    
#     try:
#        category= Category.objects.get(title=title)
       
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=='GET':
#        serializer= CategorySerializer(category)
#        return Response(serializer.data)
        
#     elif request.method=='PUT':
#         serializer= CategorySerializer(category,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
#     elif request.method=='DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
      
      

# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny,])
# def Product_list(request, format=None):
      
#     if request.method =='GET':
#        product=Product.objects.all()
#        serializer=ProductSerializer(product, many=True)
#        return Response(serializer.data)
     
#     if request.method=='POST':
#        serializer=ProductSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
     
   
# @api_view(['GET', 'PUT','DELETE'])
# def Product_detail(request,slug,format=None):
    
#     try:
#        product= Product.objects.get(new_slug=slug)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=='GET':
#        serializer= ProductSerializer(product)
#        return Response(serializer.data)
        
#     elif request.method=='PUT':
#         serializer= ProductSerializer(product,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
#     elif request.method=='DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
   



# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny,])
# def Brand_list(request, format=None):
      
#     if request.method =='GET':
#        brand=Brand.objects.all()
#        serializer=BrandSerializer(brand, many=True)
#        return Response(serializer.data)
     
#     if request.method=='POST':
#        serializer=BrandSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
     
   
# @api_view(['GET', 'PUT','DELETE'])
# def Brand_detail(request,title,format=None):
    
#     try:
#        brand= Brand.objects.get(title=title)
#     except Brand.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=='GET':
#        serializer= BrandSerializer(brand)
#        return Response(serializer.data)
        
#     elif request.method=='PUT':
#         serializer= BrandSerializer(brand,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
#     elif request.method=='DELETE':
        
#         brand.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
   



           


      
   
   

    



     
    
     
   

    
   
        
   
   


     
   
     
   

    
        
    
   


      
     
   

    
      
        
    
   

