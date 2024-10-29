from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import clothes, newss, CartItem

def index(request):
    num_clothes = clothes.objects.all().count()
    return render(request,'catalog/base.html', context={'num_clothes': num_clothes})

def Contacts(request):
    return render(request, "catalog/contacts.html")

def News(request):
    news = newss.objects.order_by('-dates')
    return render(request, "catalog/news.html", {'news': news})

def product_list(request):
    products = clothes.objects.order_by('-dates')
    return render(request, "catalog/products.html", {'products': products})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.summ * item.quantity for item in cart_items)
    return render(request, 'catalog/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = clothes.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('catalog:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('catalog:view_cart')
