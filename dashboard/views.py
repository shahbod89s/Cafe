from django.shortcuts import render, redirect, get_object_or_404
from menu.models import Order, Food
from django.contrib.auth.decorators import user_passes_test
from menu.forms import FoodForm
from django.core.management import call_command
from django.http import HttpResponse


def migrate_database(request):
    call_command("migrate")
    return HttpResponse("Migration completed!")

def dashboard_orders(request):
    orders = Order.objects.all().order_by("-created_at")

    new_orders = Order.objects.filter(
        status="new"
    ).count()


    preparing_orders = Order.objects.filter(
        status="preparing"
    ).count()


    ready_orders = Order.objects.filter(
        status="ready"
    ).count()


    context = {
        "orders": orders,
        "new_orders": new_orders,
        "preparing_orders": preparing_orders,
        "ready_orders": ready_orders,
    }


    return render(
        request,
        "dashboard/orders.html",
        context
    )
    
def update_order_status(request, id):
    order = get_object_or_404(
        Order,
        id=id
    )

    if request.method == "POST":

        status = request.POST.get(
            "status"
        )
        order.status = status
        order.save()

    return redirect(
        "dashboard"
    )
    
def admin_check(user):
    return user.is_staff

@user_passes_test(admin_check)
def dashboard_orders(request):

    orders = Order.objects.all().order_by("-created_at")

    new_orders = Order.objects.filter(status="new").count()

    preparing_orders = Order.objects.filter(status="preparing").count()

    ready_orders = Order.objects.filter(status="ready").count()

    context = {
        "orders": orders,
        "new_orders": new_orders,
        "preparing_orders": preparing_orders,
        "ready_orders": ready_orders,
    }

    return render(
        request,
        "dashboard/orders.html",
        context
    )
    
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

            return redirect(
                "foods_manage"
            )

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

            return redirect(
                "foods_manage"
            )

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

        return redirect(
            "foods_manage"
        )

    return render(
        request,
        "dashboard/delete_food.html",
        {
            "food": food
        }
    )