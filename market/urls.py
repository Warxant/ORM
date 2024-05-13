

from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', show_catalog, name='show_catalog'),
    path('catalog/<slug:slug>/', show_product, name='show_product'),
]
