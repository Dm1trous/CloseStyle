from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin

from .forms import CreateCommentForm
from .models import clothes, newss, CartItem, Post, Topic, Comment, size, color, brend, gender, cat, material
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView
)

def index(request):
    # Извлекаем фильтры
    gender_filter = request.GET.get("gender", "all")

    # Формируем список товаров согласно фильтру
    if gender_filter == "male":
        latest_products = clothes.objects.filter(genderr__name="Мужчины").order_by("-dates")[:5]
    elif gender_filter == "female":
        latest_products = clothes.objects.filter(genderr__name="Женщины").order_by("-dates")[:5]
    else:
        latest_products = clothes.objects.order_by("-dates")[:5]

    # Определяем количество товаров в корзине
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_quantity = sum(item.quantity for item in cart_items)
        return render(request, 'catalog/base.html', {
            'latest_products': latest_products,
            'num_clothes': len(latest_products),
            'total_quantity': total_quantity
        })
    else:
        return render(request, 'catalog/base.html', {
            'latest_products': latest_products,
            'num_clothes': len(latest_products)
        })



def Contacts(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_quantity = sum(item.quantity for item in cart_items)
        return render(request, "catalog/contacts.html", context={'total_quantity': total_quantity})
    else:
        return render(request, "catalog/contacts.html")

def News(request):
    news = newss.objects.order_by('-dates')
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_quantity = sum(item.quantity for item in cart_items)
        return render(request, "catalog/news.html", {'news': news, 'total_quantity': total_quantity})
    else:
        return render(request, "catalog/news.html", {'news': news})



def product_list(request):
    products = clothes.objects.order_by('-dates')
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_quantity = sum(item.quantity for item in cart_items)
        return render(request, "catalog/products.html", {'products': products, 'total_quantity': total_quantity})
    else:
        return render(request, "catalog/products.html", {'products': products})


def view_cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.summ * item.quantity for item in cart_items)
        total_quantity = sum(item.quantity for item in cart_items)
        return render(request, 'catalog/cart.html',  {'cart_items': cart_items, 'total_price': total_price, 'total_quantity': total_quantity})
    else:
        return render(request, 'catalog/cart.html')


def add_to_cart(request, product_id):
    product = clothes.objects.get(id=product_id)
    size_id = request.GET.get('size_id')
    if size_id is None or int(size_id) not in list(product.sizee.values_list('id', flat=True)):
        raise ("Нет такого размера!")

    chosen_size = size.objects.get(id=int(size_id))

    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        user=request.user,
        size=chosen_size
    )
    cart_item.quantity += 1
    cart_item.save()
    return redirect('catalog:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('catalog:view_cart')

def plus_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('catalog:view_cart')

def minus_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity -= 1
    cart_item.save()
    return redirect('catalog:view_cart')


class TopicListView(ListView):
    model = Topic
    template_name = 'forum/index.html'
    context_object_name = 'topics'

class TopicDetailView(DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(topic=self.kwargs.get('pk'))
        return context

class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title']

    def form_valid(self, form):
        return super().form_valid(form)

class PostDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Post
    form_class = CreateCommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.kwargs.get('pk'))
        context['form'] = CreateCommentForm(initial={'post': self.object, 'author': self.request.user})

        return context

    def get_success_url(self):
        return reverse('catalog:post-detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic = Topic.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/forum/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def product_detail(request, product_id):
    product = get_object_or_404(clothes, id=product_id)
    available_sizes = product.sizee.all()
    return render(request, 'catalog/product_detail.html', {'product': product, 'sizes': available_sizes})

def product_list(request):
    # Получаем параметры из GET-запроса
    sort_order = request.GET.get('sort', '')
    size_ids = request.GET.getlist('size')
    color_ids = request.GET.getlist('color')
    brand_ids = request.GET.getlist('brand')
    gender_id = request.GET.get('gender')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category_ids = request.GET.getlist('category')
    material_ids = request.GET.getlist('material')

    # Базовый queryset
    products = clothes.objects.all()

    # Фильтрация по параметрам
    if size_ids:
        products = products.filter(sizee__in=size_ids)
    if color_ids:
        products = products.filter(colorr__in=color_ids)
    if brand_ids:
        products = products.filter(brendd__in=brand_ids)
    if gender_id and gender_id != 'all':
        products = products.filter(genderr__id=gender_id)
    if category_ids:
        products = products.filter(catt__in=category_ids)
    if material_ids:
        products = products.filter(materiall__in=material_ids)
    if min_price and max_price and min_price != 'all' and max_price != 'all':
        products = products.filter(summ__gte=min_price, summ__lte=max_price)

    # Сортировка
    if sort_order == 'name_asc':
        products = products.order_by('title')
    elif sort_order == 'name_desc':
        products = products.order_by('-title')
    elif sort_order == 'price_asc':
        products = products.order_by('summ')
    elif sort_order == 'price_desc':
        products = products.order_by('-summ')

    # Контекст с товарами и доступными фильтрами
    context = {
        'products': products,
        'sizes': size.objects.all(),
        'colors': color.objects.all(),
        'brands': brend.objects.all(),
        'genders': gender.objects.all(),
        'categories': cat.objects.all(),
        'materials': material.objects.all(),
        'cat': cat.objects.all(),
        'selected_genders': gender_id,
        'selected_colors': color_ids,
        'selected_brands': brand_ids,
        'selected_sizes': size_ids,
        'selected_categories': category_ids,
        'selected_materials': material_ids,
        'min_price': min_price,
        'max_price': max_price,
        'sort_order': sort_order,
    }

    return render(request, 'catalog/products.html', context)