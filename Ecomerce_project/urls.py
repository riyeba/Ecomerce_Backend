"""
URL configuration for Ecomerce_project project.

The `urlpatterns` list routes URLs to views. For more Brandrmation please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from Ecomerce_app import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


# urlpatterns = [
    
#     path('admin/', admin.site.urls),
#     # path('category/', (views.Category_list)),
#     # path('category/<str:title>/', (views.Category_detail)),
#     #  path('product/<str:category>/', (views.Category_detail)),
#     path('product/', (views.Product_list)),
#     # path('product/<slug>', (views.Product_detail)),
#     # path('brand/', (views.Brand_list)),
#     # path('brand/<str:title>/', (views.Brand_detail)),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', views.Product_list.as_view(), name='product'),
    path('category/', views.Category_list.as_view(), name='category'),
    path('category/<int:pk>/', views.Category_detail.as_view()),
    path('carts/', views.Cart_list.as_view()),
    path('carts/<int:pk>/', views.Cart_detail.as_view()),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)