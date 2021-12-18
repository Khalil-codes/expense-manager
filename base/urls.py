from django.urls import path
from . import views

urlpatterns = [
   path('', views.HomeView, name="home"),
   path('addTransaction', views.AddTransaction, name="addTransaction"),
   path('addCategory', views.AddCategory, name="addCategory"),
   path('deleteTransaction/<int:id>', views.deleteTransaction, name='deleteTransaction'),
   path('login', views.LoginUser, name='login'),
   path('register', views.RegisterUser, name='register'),
   path('logout', views.LogoutUser, name='logout'),
]