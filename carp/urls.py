"""
URL configuration for carp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from carapp.views import *
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('carlist', car_list, name='car_list'),              # List all cars
    path('car/<int:pk>/', car_detail, name='car_detail'),  # View car details
    path('car/add/', car_create, name='car_create'),   # Add new car
    path('car/<int:pk>/edit/', car_update, name='car_update'),  # Edit car
     path('car/<int:pk>/delete/', car_delete, name='car_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)