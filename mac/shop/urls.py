from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name = 'ShopHome'),
    path('About/' , views.about , name = 'About'),
    path('Contact/' , views.contact , name = 'Contact'),
    path('Tracker/' , views.tracker , name = 'Tracker'),
    path('Search' , views.search , name = 'Search'),
    path('Products/<int:my_id>' , views.ProductView , name = 'ProductView'),
    path('Checkout' , views.checkout , name = 'Checkout'),
]
