from django.urls import path
from .views import index, dishes, dish_detail, dish_create, dish_update


urlpatterns = [
    path("", index, name="index"),
    path("dishes/", dishes, name="dishes"),
    path("dish/<pk>", dish_detail, name="dish_detail"),
    path("dish/", dish_create, name="dish_create"),
    path("update_dish/<pk>", dish_update, name="dish_update"),
]
