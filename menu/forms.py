from django import forms
from .models import Order
from django import forms
from .models import Food


class FoodForm(forms.ModelForm):

    class Meta:

        model = Food

        fields = "__all__"

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "order-input",
                    "placeholder": "نام غذا"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "order-textarea",
                    "rows": 4
                }
            ),

            "ingredients": forms.Textarea(
                attrs={
                    "class": "order-textarea",
                    "rows": 3
                }
            ),

            "price": forms.NumberInput(
                attrs={
                    "class": "order-input"
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "order-input"
                }
            ),

            "image": forms.TextInput(
                attrs={
                    "class": "order-input",
                    "placeholder": "مثال: pizza.webp"
                }
            ),

        }

class OrderForm(forms.ModelForm):

    class Meta:

        model = Order

        fields = (
            "customer_name",
            "phone",
            "table_number",
            "quantity",
            "note",
        )

        labels = {
            "customer_name": "نام و نام خانوادگی",
            "phone": "شماره تماس",
            "table_number": "شماره میز",
            "quantity": "تعداد",
            "note": "توضیحات",
        }

        widgets = {
            "customer_name": forms.TextInput(
                attrs={
                    "class": "order-input",
                    "placeholder": "نام خود را وارد کنید"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "order-input",
                    "placeholder": "09xxxxxxxxx"
                }
            ),

            "table_number": forms.NumberInput(
                attrs={
                    "class": "order-input",
                    "placeholder": "شماره میز",
                    "min": 1
                }
            ),

            "quantity": forms.NumberInput(
                attrs={
                    "class": "order-input",
                    "min": 1,
                    "value": 1
                }
            ),

            "note": forms.Textarea(
                attrs={
                    "class": "order-textarea",
                    "rows": 4,
                }
            ),
        }