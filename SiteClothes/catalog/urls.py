from django.urls import path, re_path, include
from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.News, name='news'),
    path('contacts/', views.Contacts, name='contacts'),
    path('cart/', views.view_cart, name='view_cart'),
    path('products/', views.product_list, name='view_product'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]