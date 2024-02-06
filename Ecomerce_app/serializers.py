from rest_framework import serializers
from .models import Category,Product,Brand,Cart


class ProductSerializer(serializers.ModelSerializer):
  
  class Meta:
    model=Product
    fields=['id','title','new_slug','price','promo_price','stock','status','brand','image_URL','date_created','category','quantity']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
     model=Category
     fields=['id','products','category_url','categoryname']
    

    
class BrandSerializer(serializers.ModelSerializer):
  product = ProductSerializer(many=True, read_only=True)
  class Meta:
    model=Brand
    fields=['id','title','product']
    

class CartSerializer(serializers.ModelSerializer):
  class Meta:
    model=Cart
    fields=['id','title','new_slug','price','promo_price','stock','status','brand','image_URL','date_created','quantity'] 
    

    
