from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from .models import Expense, UserProfile, Categories
from .decorators import unauthenticated_user


# Create your views here.

# Authentocation
@unauthenticated_user
def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credentials Incorrect')
            return redirect('login')

    return render(request, 'auth/login.html')

@unauthenticated_user
def RegisterUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        balance = request.POST.get('balance')
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, balance=balance, income=balance).save()
            messages.success(request, f'Account Created!')
            return redirect('login')
    else:
        form = CreateUserForm()

    context = { 
        'form':form,
    }
    return render(request, 'auth/register.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('login')

def is_valid_queryparam(param):
    return param != '' and param is not None

@login_required(login_url='login')
def HomeView(request):
    userProfile = UserProfile.objects.get(user = request.user)
    expenses = Expense.objects.filter(user = request.user)
    categories = Categories.objects.all()
    category = request.GET.get('category')

    # For Filtering
    if is_valid_queryparam(category) and category != 'all':
        expenses = expenses.filter(category__name=category)
    
    context = {
        'user_profile':userProfile,
        'expenses':expenses,
        'categories':categories,
    }
    return render(request, 'base/home.html',context)

def AddTransaction(request):
    userProfile = UserProfile.objects.get(user = request.user)

    if request.POST:
        # Getting the Input values and Updating in Expense Model
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        transaction_type = request.POST.get('transaction-type')
        if int(amount) > userProfile.balance:
                messages.error(request, "Amount Exceeds your Balance")
                return redirect('home')
        expense = Expense(user=request.user,description=description, category=Categories.objects.get(name=category), cost=amount, type=transaction_type)
        expense.save()
        # Updating Balance, Income and Expenses
        if transaction_type == 'Expense':
            userProfile.balance -= int(amount)
            userProfile.expenses += int(amount)
        else:
            userProfile.balance += int(amount)
            userProfile.income += int(amount)

        userProfile.save()

    return redirect('home')

def deleteTransaction(request, id):
    Expense.objects.get(id = id).delete()
    return redirect('home')

def AddCategory(request):
    if request.POST:
        category = request.POST.get('category').capitalize()
        print(category)
        Categories.objects.create(name=category).save()
    return redirect('home')