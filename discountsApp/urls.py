from django.urls import path
from . import views

app_name = 'discountsApp'
urlpatterns = [
    path('', views.index, name='discounts-main'),
    path('all/',views.allPorduct),
    path('luxury/',views.luxury),
    path('electronic/',views.electronic),
    path('clothing/',views.clothing),
    path('lastChance/',views.lastChancePage),
    path('addproduct/<int:id>/', views.add_to_wishlist, name='add-product'),
    path('removeproduct/<int:id>/', views.remove_from_wishlist, name='remove-product'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('search/', views.search, name='search'),
]
