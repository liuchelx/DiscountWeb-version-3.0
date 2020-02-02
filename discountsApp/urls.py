from django.urls import path
from . import views

app_name = 'discountsApp'
urlpatterns = [
    path('', views.index, name='discounts-main'),
    # path('login/', views.login),
    # path('signup/', views.signup),
    # path('forgotpassword/', views.forgotPassword),
    #path('product/',views.product),
    path('all/',views.allPorduct),
    path('luxury/',views.luxury),
    path('electronic/',views.electronic),
    path('clothing/',views.clothing),
    path('lastChance/',views.lastChancePage),
    path('addproduct/<int:id>/', views.add_to_wishlist, name='add-product'),
    path('removeproduct/<int:id>/', views.remove_from_wishlist, name='remove-product'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('searchResult/', views.search, name='search'),
   # path('addproduct/done', views.add_to_wishlist_done, name='add-product-done'),
]
