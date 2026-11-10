from django.shortcuts import render, redirect
from .models import *


def get_categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})


def add_category(request):
    if request.method == "POST":
        Category.objects.create(
            name=request.POST["name"]
        )
        return redirect("categories")
    return render(request, "add_category.html")


def get_dishes(request):
    dishes = Dishes.objects.all()
    return render(request, "dishes.html", {"dishes": dishes})


def add_dish(request):
    categories = Category.objects.all()

    if request.method == "POST":
        dish = Dishes.objects.create(
            name=request.POST["name"],
            caption=request.POST["caption"],
            price=request.POST["price"]
        )
        dish.cateory.add(request.POST["category"])
        return redirect("dishes")
    return render(request, "add_dish.html", {"categories": categories})

def get_tables(request):
    tables = Table.objects.all()
    return render(request, "tables.html", {"tables": tables})


def add_table(request):
    if request.method == "POST":
        Table.objects.create(
            table_num=request.POST["table_num"],
            username=request.POST["username"]
        )
        return redirect("tables")
    return render(request, "add_table.html")


def get_orders(request):
    orders = Orders.objects.all()
    return render(request, "orders.html", {"orders": orders})


def get_order_id(request, id):
    order = Orders.objects.get(pk=id)
    return render(request, "order_detail.html", {"order": order})


def delete_order(request, id):
    order = Orders.objects.get(pk=id)

    if request.method == "POST":
        order.delete()
        return redirect("orders")

    return render(request, "delete_order.html", {"order": order})
