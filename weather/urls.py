from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.func, name='func'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),

]