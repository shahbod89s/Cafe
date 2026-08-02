from django.shortcuts import render, get_object_or_404
from .models import Food, Order
from .forms import OrderForm


def menu_page(request, category=None):

    if category:
        foods = Food.objects.filter(
            category=category
        )

    else:
        foods = Food.objects.all()

    context = {
        "foods": foods
    }

    return render(
        request,
        "menu/index.html",
        context
    )

def food_detail(request, id):
    food = get_object_or_404(
        Food,
        id=id
    )

    success = False

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.food = food
            order.save()
            success = True
            form = OrderForm()

    else:
        form = OrderForm()


    context = {
        "food": food,
        "form": form,
        "success": success,
    }

    return render(
        request,
        "menu/detail.html",
        context
    )