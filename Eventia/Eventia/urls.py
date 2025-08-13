from django.contrib import admin
from django.urls import path
from eventia_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
]
