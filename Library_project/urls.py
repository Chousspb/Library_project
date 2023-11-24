from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from library.views import book_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('books/')),
    path('api/', include('library.urls')),
    path('books/', book_list, name='book_list')
]
