from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyBookListView.as_view(), name='my_book_list'),

    # URL for displaying the details of a specific book
    path('my_book_list/<int:id>/', views.MyBookDetailView.as_view(), name='my_book_detail'),

    # URL for listing books with edit option
    path('book_list_edit/', views.BookListEditView.as_view(), name='book_list_edit'),

    # URL to update a specific book
    path('update_book/<int:id>/', views.UpdateBookView.as_view(), name='update_book'),

    # URL to list books for deletion
    path('my_book_list_delete/', views.MyBookListDeleteView.as_view(), name='my_book_list_delete'),

    # URL to delete a specific book
    path('book_drop/<int:id>/', views.BookDropView.as_view(), name='book_drop'),

    # URL to create a new book
    path('create_book/', views.CreateBookView.as_view(), name='create_book'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('my_book_list/<int:id>/delete/', views.BookDropDeleteView.as_view()),


]
