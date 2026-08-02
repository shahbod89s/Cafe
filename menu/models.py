from django.db import models


class Food(models.Model):

    CATEGORY_CHOICES = [
        ("main", "غذای اصلی"),
        ("drink", "نوشیدنی"),
        ("dessert", "دسر"),
    ]

    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    ingredients = models.TextField(
        blank=True
    )

    price = models.IntegerField()

    image = models.ImageField(
        upload_to="foods/"
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="main"
    )

    is_special = models.BooleanField(
        default=False
    )

    is_available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name





class Order(models.Model):

    STATUS_CHOICES = [
        ("new", "جدید"),
        ("preparing", "در حال آماده‌سازی"),
        ("ready", "آماده"),
        ("done", "تحویل داده شد"),
    ]

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    customer_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=20
    )

    table_number = models.PositiveIntegerField()

    quantity = models.PositiveIntegerField(
        default=1
    )

    note = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.customer_name} - {self.food.name}"