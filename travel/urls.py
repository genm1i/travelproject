from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tours/', views.tours, name='tours'),
    path('tour/<int:id>/', views.tour_detail, name='tour_detail'),

    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('send-request/', views.send_request, name='send_request'),
]