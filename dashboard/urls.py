from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path(
        "migrate-948372/",
        views.migrate_database,
        name="migrate_database"
    ),
    path(
        "create-admin-948372/",
        views.create_admin,
        name="create_admin"
    ),
    path(
        "",
        views.dashboard_orders,
        name="dashboard"
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="dashboard/login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),
    
    path(
        "foods/",
        views.foods_manage,
        name="foods_manage"
    ),
    
    path(
        "foods/add/",
        views.add_food,
        name="add_food"
    ),
    path(
        "foods/edit/<int:id>/",
        views.edit_food,
        name="edit_food"
    ),
    path(
        "foods/delete/<int:id>/",
        views.delete_food,
        name="delete_food"
    ),
]