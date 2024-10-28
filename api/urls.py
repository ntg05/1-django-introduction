from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/introspect/', views.TokenIntrospectView.as_view(), name='token-introspect'),
    path('dishes/', views.DishList.as_view(), name='dish-list'),
    path('dish/<int:pk>/', views.DishDetail.as_view(), name='dish-detail'),
    path('restaurants/', views.RestaurantList.as_view(), name='restaurant-list'),
    path('restaurant/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurant-detail'),
    path('menu/<int:pk>/', views.MenuDetail.as_view(), name='menu-detail'),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('order_items/', views.OrderItemList.as_view(), name='order-item-list'),
    path('api/order_item/<int:pk>/', views.OrderItemDetail.as_view(), name='order-item-detail'),
]
