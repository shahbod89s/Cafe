from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.menu_page,
        name="menu"
    ),

    path(
        "category/<str:category>/",
        views.menu_page,
        name="category"
    ),

    path(
        "food/<int:id>/",
        views.food_detail,
        name="food_detail"
    ),
]