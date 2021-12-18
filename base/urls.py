from django.urls import path
from . import views

urlpatterns = [
   path('', views.HomeView, name="home"),
   path('addTransaction', views.AddTransaction, name="addTransaction"),
   path('deleteTransaction/<int:id>', views.deleteTransaction, name='deleteTransaction')
]