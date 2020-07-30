from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from books.views import *
from django.conf.urls import url
from shoping import views as views

app_name = 'shopping_cart'



urlpatterns = [
    path('', views.index, name='index'),
    path('<str:title>', views.bookDetails, name='bookDetails'),
    path('topsell/', views.top_sell, name= 'top_sell' ),
    path('general/<str:gname>/', views.book_general, name= 'book_general'),
    path('rating/<int:filter>/', views.book_rating, name= 'book_rate' ),
    path('ordering/<int:filter>/', views.book_order, name= 'book_order' ),
    path('add_to_cart/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('order_summary/', views.order_details, name='summary'),
    path('item/delete/<item_id>', views.delete_from_cart, name='delete_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-quantity-from-cart/<item_id>', views.add_quantity_from_cart, name='add_quantity_from_cart'),
    path('reduce-quantity-from-cart/<item_id>', views.reduce_quantity_from_cart, name='reduce_quantity_from_cart'),
    path('save-item/<item_id>', views.save_item, name='save_item'),
    path('add-back-item/<item_id>', views.add_back_item, name='add_back_item'),
    path('booklist/',views.index, name='booklist'),
    path('author-list/<author>' , views.author_book_list, name='author_book_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

