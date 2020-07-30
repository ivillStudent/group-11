from django.contrib import admin
from .models import Book, General, Author, Order, OrderItem
from django.apps import apps

class GeneralAdmin(admin.ModelAdmin):
    list_display = ['name']
   
admin.site.register(General, GeneralAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'bio', 'date_of_birth']
   
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'author','cover', 'published_date', 'publishing_info','price','top_sell', 'book_rate']
    list_filter = ['top_sell', 'book_rate']
  
admin.site.register(Book, BookAdmin)

admin.site.register(Order) 
admin.site.register(OrderItem)
admin.site.register(Author) 
admin.site.register(Book)
admin.site.register(General)  
