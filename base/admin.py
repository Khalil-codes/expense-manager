from django.contrib import admin
from . import models
# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
     list_display = ('description', 'type', 'category', 'cost', 'user', 'date')
 
admin.site.register(models.Expense, ExpenseAdmin)
admin.site.register(models.UserProfile)
admin.site.register(models.Categories)