
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('Product.urls')),  # Подключаем маршруты для Product
    path('my_books/', include('my_book.urls')),
    path('user/', include('users.urls')),# Подключаем маршруты для MyBook
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
