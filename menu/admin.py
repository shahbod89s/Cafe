from django.contrib import admin
from .models import Food, Order


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "category",
        "is_special",
        "is_available",
    )

    list_filter = (
        "category",
        "is_special",
        "is_available",
    )

    search_fields = (
        "name",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "food",
        "table_number",
        "quantity",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "customer_name",
        "phone",
    )

    ordering = (
        "-created_at",
    )