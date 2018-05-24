from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=15,primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Item(models.Model):
    user_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=50)
    terms = models.CharField(max_length=30)
    location = models.CharField(max_length=15)
    delivery = models.BooleanField(default=False)
    deposit = models.IntegerField()
    cost_per_week = models.IntegerField()

    def __str__(self):
        return self.title
