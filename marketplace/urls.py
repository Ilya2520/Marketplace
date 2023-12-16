from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import ClientList, OrderList, DeliveryList, GoodsList, OrderStructList, StorageList, register, order_detail, \
    search, storage_search
from .views import clients, orders, goods, storages, deliveries, index
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('api/clients/', ClientList.as_view(), name='client-list'),
    path('api/order_structs/', OrderStructList.as_view(), name='order_struct-list'),
    path('api/orders/', OrderList.as_view(), name='order-list'),
    path('api/goods/', GoodsList.as_view(), name='goods-list'),
    path('api/storages/', StorageList.as_view(), name='storage-list'),
    path('api/delivery/', DeliveryList.as_view(), name='delivery-list'),
    path('', index, name='index'),
    path('clients/', clients, name='clients'),
    path('orders/', login_required(orders), name='orders'),
    path('orders/<int:order_id>/', order_detail, name='ord_struct'),
    path('goods/', goods, name='goods'),
    path('storages/', storages, name='storages'),
    path('deliveries/', deliveries, name='deliveries'),
    path('register/', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='marketplace/temp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', search, name='search'),
    path('storage_search/', storage_search, name='storage_search'),
]
