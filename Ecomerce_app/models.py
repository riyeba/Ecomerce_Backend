
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Category(models.Model):
  title=models.CharField(max_length=500)
  def __str__(self):
        return self.title 


      
  
class Brand(models.Model):
  title=models.CharField(max_length=500)
  def __str__(self):
        return self.title 
      
# class Product_Details(models.Model):
#     description = ArrayField(ArrayField(models.IntegerField()))
#     def __str__(self):
#         return self.description
      
# class Specification(models.Model):
#     specification = ArrayField(ArrayField(models.IntegerField()), blank=True)
    
#     def __str__(self):
#         return self.specification 
   
  
# class Key_Features(models.Model):
#     description = ArrayField(ArrayField(models.IntegerField()))
#     def __str__(self):
#         return self.description 
    
  

class Product(models.Model):
    title = models.CharField(max_length=500)
    price = models.IntegerField()
    promo_price=models.IntegerField()
    stock=models.IntegerField()
    status=models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name="product")
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE,related_name="product")
    specification=ArrayField(
        ArrayField(
            models.CharField(max_length=200, blank=True),
           
        ),
       
    )
    key_features = ArrayField(
        ArrayField(
            models.CharField(max_length=200, blank=True),
            
        ),
        
    )
    detail= ArrayField(
        ArrayField(
            models.CharField(max_length=200, blank=True),
            
        ),
        
    )
    image_URL= models.URLField()
    date_created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} {self.price}"
    
    class Meta:
        ordering = ["date_created"]


   
  

   
  

    
   
  
  