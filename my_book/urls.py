from django.urls import path
from . import views

urlpatterns = [
    path('my_book_list/', views.my_book_list_view, name='my_book_list'),
    path('my_book_list/<int:id>/', views.my_book_detail_view, name='my_book_detail'),
]
