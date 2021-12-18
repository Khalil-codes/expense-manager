from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    income = models.IntegerField()
    expenses = models.IntegerField(default=0)
    balance = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username.capitalize()

class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Expense(models.Model):
    EXPENSETYPE = {
        ('Expense', 'Expense'),
        ('Income', 'Income'),
    }
    user = models.ForeignKey(User, on_delete=CASCADE)
    description = models.CharField(max_length=50)
    cost = models.IntegerField(default=True)
    category = models.ForeignKey(Categories,on_delete=CASCADE, blank=True, null=True)
    type = models.CharField(max_length=50, default='Expense', choices=EXPENSETYPE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    @property
    def isExpense(self):
        return (self.type == 'Expense')
