from django.urls import path, include
from .views import *

urlpatterns = [
   path('get-product/',getProduct),
   path('add-product/',addProduct),
   path('single-product-detail/<int:product_id>',singleProductDetail),
   path('edit-product/<int:product_id>',editProduct),
   path('delete-product/<int:product_id>',deleteProduct),
]

