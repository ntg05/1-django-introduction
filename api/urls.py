from django.urls import path

from api import views


urlpatterns = [
    path('dishes/', views.DishViewSet.as_view()),
]
