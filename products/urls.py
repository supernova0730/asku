from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('reviews/', views.reviews, name='reviews'),

    path('products/', views.product_list, name='product_list'),
    path('product/<int:position_code>/', views.product_detail, name='product_detail'),

    path('basket/', views.basket, name='basket'),
    path('basket-form/', views.basket_form, name='basket-form')
]
