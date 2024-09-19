from django.urls import path
from . import views

urlpatterns = [
    path('filter_list/', views.product_filter_view, name='product_filter'),
]
