from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Product
from django.http import Http404
# Create your views here.
# def index(request):
#     template=loader.get_template('productapp\index.html')
#     products=Product.objects.all
#     context={
#         "message":"Products title",
#         "products":products
#     }
#     display = template.render(context=context,request=request)
#     return HttpResponse(display)

def details(request,product_id):
    try:
        product=Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("products does not exist")
    template=loader.get_template('productapp\detail.html')
    context={
        "product":product
    }
    display = template.render(context=context,request=request)
    return HttpResponse(display)

def about(request):
    return render(request, 'productapp/about.html')

def contact(request):
    return render(request, 'productapp/contact.html')

def product(request):
    #return render(request, 'productapp/product.html')
    template=loader.get_template('productapp\product.html')
    products=Product.objects.all
    context={
        "message":"Products title",
        "products":products
    }
    display = template.render(context=context,request=request)
    return HttpResponse(display)



def home(request):
    return render(request, 'productapp/home.html')






