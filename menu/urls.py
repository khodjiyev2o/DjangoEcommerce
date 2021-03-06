from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import ProductDetailView, AuthorCreateView, AuthorUpdateView, CustomerView, AuthorDeleteView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    # STORE
    path('', views.menu, name='menu'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('<int:pk>/view', ProductDetailView.as_view(), name='viewpage'),
    path('customers', CustomerView.as_view(), name='users'),
    # REGISTRATION
    path('login', views.thelogin, name='login'),
    path('register', views.register, name='register'),
    path('logout_user', views.logout_user, name='logout_user'),

    # USERCREATE
    path('create', AuthorCreateView.as_view(), name='create'),
    path('<int:pk>/update', AuthorUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', AuthorDeleteView.as_view(), name='delete'),
    path('<int:pk>/profile', views.profileupdate, name='profile'),

    # PASSWORD RESET
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='reset-password'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    # API
    path('api/products/<int:pk>/', views.ProductDetail.as_view(), name='products'),
    path('api/products/', views.ProductDetail.as_view(), name='productss'),
    path('api/products/create', views.ProductCreate.as_view(), name='productscreate'),
    path('api/orderitems/', views.OrderItemApiView.as_view(), name='orderitems'),
    path('api/orderitem/update/', views.OrderUpdateApiView.as_view(), name='orderitemupdate'),
    path('api/orderitems/<int:pk>', views.OrderRetrieveApiView.as_view(), name='orderitem'),
    path('api/customers/', views.CustomerApiView.as_view(), name='customers'),

    # Token
    path('auth',obtain_auth_token),


]
