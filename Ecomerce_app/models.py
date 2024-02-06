
from django.db import models
from django.contrib.postgres.fields import ArrayField
from autoslug import AutoSlugField
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
  categoryname=models.CharField(max_length=500)
  category_url=models.URLField()
  def __str__(self):
        return self.categoryname

  
class Brand(models.Model):
  brandname=models.CharField(max_length=500)
  def __str__(self):
        return self.brandname
      


class Product(models.Model):
    title = models.CharField(max_length=255)
    new_slug = AutoSlugField(populate_from='title', unique=True, null=True,default=None, max_length=255)
    price = models.IntegerField()
    promo_price=models.IntegerField()
    stock=models.IntegerField()
    status=models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products")
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE,related_name="product")
    # specification=models.CharField(max_length=500)
    # key_features = models.CharField(max_length=500)
    # detail=models.CharField(max_length=500)
    image_URL= models.URLField()
    date_created=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
    
    

        
    
    class Meta:
        ordering = ["date_created"]


class Cart(models.Model):
    title = models.CharField(max_length=255)
    new_slug = AutoSlugField(populate_from='title', unique=True, null=True,default=None, max_length=255)
    price = models.IntegerField()
    promo_price=models.IntegerField()
    stock=models.IntegerField()
    status=models.BooleanField(default=True)
    Category= models.CharField(max_length=255)
    brand=models.CharField(max_length=255)
    # specification= models.CharField(max_length=500, blank=True),
    # key_features = models.CharField(max_length=500, blank=True),
    # detail= models.CharField(max_length=500, blank=True),
    image_URL= models.URLField()
    date_created=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
  

   
  

    
   
  
  