from django.urls import path
from . import views
urlpatterns =[
    path("",views.home,name="home"),
    path("<int:product_id>",views.details,name="details"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
     path('product/', views.product, name='product'),
    
  
]