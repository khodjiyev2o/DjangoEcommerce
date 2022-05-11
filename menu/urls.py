
from django.urls import path
from . import views
from .views import ProductDetailView
urlpatterns = [
    path('',views.menu,name='menu'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('<int:pk>/view',ProductDetailView.as_view() , name='viewpage'),
    path('login', views.thelogin, name='login'),
    path('register', views.register, name='register'),
    path('logout_user', views.logout_user, name='logout_user'),

]