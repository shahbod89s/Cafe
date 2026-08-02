from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test

from django.utils import timezone
from collections import defaultdict

from menu.models import Order, Food
from menu.forms import FoodForm


def admin_check(user):
    return user.is_staff


@user_passes_test(admin_check)
def dashboard_orders(request):

    context = {

        "new_orders":
            Order.objects.filter(
                status="new"
            ),

        "preparing_orders":
            Order.objects.filter(
                status="preparing"
            ),

        "ready_orders":
            Order.objects.filter(
                status="ready"
            ),

    }


    return render(
        request,
        "dashboard/orders.html",
        context,
    )



@user_passes_test(admin_check)
def update_order_status(request, id):

    order = get_object_or_404(
        Order,
        id=id,
    )


    if request.method == "POST":

        order.status = request.POST.get("status")

        order.save()


    return redirect("dashboard")



@user_passes_test(admin_check)
def foods_manage(request):

    foods = Food.objects.all()


    return render(
        request,
        "dashboard/foods.html",
        {
            "foods": foods
        }
    )



@user_passes_test(admin_check)
def add_food(request):

    if request.method == "POST":

        form = FoodForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            form.save()

            return redirect("foods_manage")


    else:

        form = FoodForm()



    return render(
        request,
        "dashboard/add_food.html",
        {
            "form": form
        }
    )



@user_passes_test(admin_check)
def edit_food(request, id):

    food = get_object_or_404(
        Food,
        id=id
    )


    if request.method == "POST":

        form = FoodForm(
            request.POST,
            request.FILES,
            instance=food
        )


        if form.is_valid():

            form.save()

            return redirect("foods_manage")


    else:

        form = FoodForm(
            instance=food
        )



    return render(
        request,
        "dashboard/edit_food.html",
        {
            "form": form,
            "food": food,
        }
    )



@user_passes_test(admin_check)
def delete_food(request, id):

    food = get_object_or_404(
        Food,
        id=id
    )


    if request.method == "POST":

        food.delete()

        return redirect("foods_manage")



    return render(
        request,
        "dashboard/delete_food.html",
        {
            "food": food
        }
    )



@user_passes_test(admin_check)
def completed_orders(request):

    orders = Order.objects.filter(
        status="done"
    ).order_by("-created_at")


    grouped_orders = defaultdict(list)


    for order in orders:

        date = timezone.localtime(
            order.created_at
        ).date()


        grouped_orders[date].append(order)



    return render(
        request,
        "dashboard/completed_orders.html",
        {
            "grouped_orders": dict(grouped_orders)
        }
    )