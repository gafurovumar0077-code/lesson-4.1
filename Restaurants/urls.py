from django.urls import path
from .views import *

urlpatterns = [
    path("add_dish", add_dish, name="add dish"),
    path("add_category", add_category, name="add category")
]