from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import f
from datetime import date
import random
import string
import time
from .models import Book, General, Author, Order, OrderItem
from users.models import Profile
from django import forms
from django.http import HttpResponseRedirect




def NewUser(request):
    allBook = Book.objects.all()
    return render(request, 'BookDetails/index.html', {'Booklist': allBook})


def book_list(request, author):
    try:
        athing = Author.objects.get(id=author)
    except Author.DoesNotExist: athing = None
    Books = Book.objects.filter(author=athing)
    
    paginate_by = request.GET.get('paginate_by', 10)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    general_list =  General.objects.all()
    sorted_list = [books.id for books in Books]
    request.session['bookset'] = sorted_list

    context = {'Book': Books,'page_object': page_object,'general_list': general_list,}
    
    
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {'Book': Books,'page_object': page_object,'general_list': general_list,'current_order_products': current_order_products}
        return render(request, "BookDetails/index.html", context)


def index(request):
    Books = Book.objects.all()
    paginate_by = request.GET.get('paginate_by', 15)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    general_list = General.objects.all()

    sorted_list = [books.id for books in Books]
    request.session['querset'] = sorted_list

    context = {'Book': Books,'page_object': page_object,'general_list': general_list,}
    
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {'Book': Books,'page_object': page_object,'general_list': general_list,'current_order_products': current_order_products,}
        return render(request, "BookDetails/index.html", context)


def book_info(request, bookname):
    Books = Book.objects.filter(genre__name=bookname)
    paginate_by = request.GET.get('paginate_by', 15)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    general_list = General.objects.all()

    sorted_list = [books.id for books in Books]
    request.session['querset'] = sorted_list

    context = {'Book': Books,'page_object': page_object,'general_list': general_list,}
    
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {'Book': Books,'page_object': page_object,'general_list': general_list,'current_order_products': current_order_products}
        return render(request, "BookDetails/index.html", context)


def top_sell(request):
    Books = Book.objects.filter(top_sell=True)
    paginate_by = request.GET.get('paginate_by', 15)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    general_list = General.objects.all()

    sorted_list = [books.id for books in Books]
    request.session['querset'] = sorted_list

    context = {'Book': Books,'page_object': page_object,'general_list': general_list,}
 
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {'Book': Books,'page_object': page_object,'current_order_products': current_order_products,'general_list': general_list,}
        return render(request, "BookDetails/index.html", context)


def book_rate(request, filter):
    if
    {
        filter == 1:
        Books = Book.objects.filter(rating=1)
    }
    else if 
    {
        filter == 2:
        Books = Book.objects.filter(rating=2)
    }
    else if 
    {
        filter == 3:
        Books = Book.objects.filter(rating=3)
    }
    else if 
    {
        filter == 4:
        Books = Book.objects.filter(rating=4)
    }
    else if 
    {
        filter == 5:
        Books = Book.objects.filter(rating=5)
    }
    else
    {
        Books = Book.objects.all()
    }
    
    paginate_by = request.GET.get('paginate_by', 15)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    general_list = General.objects.all()
    sorted_list = [books.id for books in Books]
    request.session['querset'] = sorted_list
    
    context = {'Book': Books,'page_object': page_object,'general_list': general_list,}
    
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [
                product.product for product in user_order_items]

        context = {'Book': Books,'page_object': page_object,'general_list': general_list,'current_order_products': current_order_products}
        return render(request, "BookDetails/index.html", context)




def book_order(request, filter=null):
    sorted_list = [Book.objects.get(id=id) for id in request.session['querset']]

    if 
    {
        filter == 1:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('book_name')
    }
    else if
    {
        filter == 2:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('-book_name')
    } 
    else if 
    {
        filter == 3:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('User')
    }
    else if 
    {
        filter == 4:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('-User')
    }
    else if 
    {
        filter == 5:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('price')
    }
    else if 
    {
        filter == 6:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('-price')
    }
    else if 
    {
        filter == 7:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('published_date')
    }
    else if 
    {
        filter == 8:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('-published_date')
    }
    
    else
    {
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('-rating')
    }
        
    paginate_by = request.GET.get('paginate_by', 15)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    general_list = General.objects.all()

    

    context = {'Book': Books,'page_object': page_object,'general_list': general_list,'sorted_list': sorted_list,}
    
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {'Book': Books,'page_object': page_object,'general_list': general_list,'current_order_products': current_order_products,'sorted_list': sorted_list,}
        return render(request, 'BookDetails/index.html', context)


@login_required()
def save_item(request, item_id):
    item_to_add = OrderItem.objects.filter(pk=item_id).update(is_saved=True)
    messages.info(request, "This book saved for later.")
    return redirect(reverse('summary'))


@login_required()
def add_back_item(request, item_id):
    item_to_add = OrderItem.objects.filter(pk=item_id).update(is_saved=False)
    messages.info(request, "This book is added back to cart.")
    return redirect(reverse('summary'))


def BookInfo(request, title):
    book = get_object_or_404(Book, book_name=title)
    generla_list = Genre.objects.all()
    
    if not request.user.is_authenticated:
        context = {'Book': book,'general_list': general_list,}
        return render(request, 'BookDetails/bookDetails.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {'Book': book,'current_order_products': current_order_products,'general_list': general_list,}
        return render(request, "BookDetails/bookDetails.html", context)



def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(time.time.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str


def get_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile)
    if order.exists():
        return order[0]
        return 0


@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = Book.objects.filter(id=kwargs.get('item_id', "")).first()
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=user_profile)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()

    messages.info(request, "This item has been added to cart")
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect(reverse('Book:product-list'))


@login_required()
def add_quantity_from_cart(request, item_id):
    item_to_add = OrderItem.objects.filter(
        pk=item_id).update(quantity=F('quantity') + 1)
    messages.info(request, "This books quantity are added.")
    return redirect(reverse('shopping_cart:order_summary'))


@login_required()
def reduce_quantity_from_cart(request, item_id):
    item_to_reduce = OrderItem.objects.filter(pk=item_id)
    if item_to_reduce[0].quantity < 3:
        item_to_reduce[0].delete()
        messages.info(request, "Book has been removed since quantity is less than 1")
    else
        item_to_reduce.update(quantity=F('quantity') - 1)
        messages.info(request, "This books quantity has been reduced.")
    return redirect(reverse('shopping_cart:order_summary'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "The book has been removed")
        return redirect(reverse('shopping_cart:order_summary'))


@login_required()
def order_details(request, **kwargs):
    general_list = General.objects.all()
    existing_order = get_user_pending_order(request)
    context = {'order': existing_order,'general_list': general_list,}
    return render(request, 'BookDetails/order_summary.html', context)


@login_required()
def checkout(request,**kwargs):
    OrderItem.objects.filter(is_saved=False).delete()
    messages.info(request, "Thank you for your business, have a good day!")
    return redirect(reverse('shopping_cart:order_summary'))
