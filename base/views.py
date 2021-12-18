from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Expense, UserProfile, Categories

# Create your views here.
def HomeView(request):
    userProfile = UserProfile.objects.get(user = request.user)
    expenses = Expense.objects.filter(user = request.user)
    categories = Categories.objects.distinct().filter(expense__user = request.user)
    categorical_cost = {}
    for expense in expenses:
        try:
            categorical_cost[expense.category.name]['amount'] += int(expense.cost)
        except:
            categorical_cost[expense.category.name] = {'name':expense.category.name, 'amount':expense.cost}
    
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
        expense = Expense(user=request.user,description=description, category=category, cost=amount, type=transaction_type)
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