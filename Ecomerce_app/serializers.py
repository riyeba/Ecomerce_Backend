from rest_framework import serializers
from .models import Category,Product,Brand


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model=Category
    fields=['id','title']
    

    
class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model=Brand
    fields=['id','title']
    
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model=Product
    fields=['id','title','price','promo_price','stock','status','category','brand','image_URL','detail','specification','key_features','date_created']
  
    
# class Product_DetailsSerializer(serializers.ModelSerializer):
#   class Meta:
#     model=Product_Details
#     fields=['id','title','description']
    
# class SpecificationSerializer(serializers.ModelSerializer):
#   class Meta:
#     model=Specification
#     fields=['id','description']
    
# class Key_FeaturesSerializer(serializers.ModelSerializer):
#   class Meta:
#     model=Key_Features
#     fields=['id','title','description']
    
