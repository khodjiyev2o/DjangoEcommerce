
from django.urls import path
from . import views
from .views import ProductDetailView,AuthorCreateView,AuthorUpdateView,AuthorDeleteView
urlpatterns = [
    path('',views.menu,name='menu'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('<int:pk>/view',ProductDetailView.as_view() , name='viewpage'),
    path('login', views.thelogin, name='login'),
    path('register', views.register, name='register'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('create', AuthorCreateView.as_view(), name='create'),
    path('<int:pk>/update', AuthorUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', AuthorDeleteView.as_view(), name='delete'),
    path('<int:pk>/profile', views.profileupdate, name='profile'),

]