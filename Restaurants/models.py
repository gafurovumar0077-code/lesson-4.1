from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Dishes(models.Model):
    cateory = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=160)
    price = models.IntegerField()


class Table(models.Model):
    table_num = models.IntegerField()
    username = models.CharField()


class Orders(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    dishes = models.ManyToManyField(Dishes)
    created_at = models.DateTimeField(auto_now_add=True)