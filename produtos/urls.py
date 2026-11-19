from django.urls import path

from . import views

urlpatterns = [
    path('novo/', views.produto_new, name='produto_new'),
    path('produtos/', views.produto_list, name='produto_list'),
]