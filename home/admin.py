from django.contrib import admin
from .models import Expense, Income

# Register your models here.

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    display_list = ["title", "user", "amount", "date"]


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    display_list = ["title", "user", "amount", "date"]