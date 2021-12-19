import django_filters
from .models import Expense
from django import forms

class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = ['category',]
