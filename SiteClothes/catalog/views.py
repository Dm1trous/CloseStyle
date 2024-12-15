from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin

from .forms import CreateCommentForm
from .models import clothes, newss, CartItem, Post, Topic, Comment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView
)

def index(request):
    num_clothes = clothes.objects.all().count()
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_quantity = sum(item.quantity for item in cart_items)
        return render(request,'catalog/base.html', context={'num_clothes': num_clothes, 'total_quantity': total_quantity})
    else:
        return render(request, 'catalog/base.html',context={'num_clothes': num_clothes})



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
    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                       user=request.user)
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
