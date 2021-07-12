from django.contrib import admin
from .models import *
from .main_admin import grand_budget_admin
from .forms import PositionForm




# @admin.register(Personnel, site=grand_budget_admin)
# class PersonnelAdmin(admin.ModelAdmin):
#     pass


# @admin.register(DepartmentBudget, site=grand_budget_admin)
# class DepartmentAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Department, site=grand_budget_admin)
# class DepartmentAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Grant, site=grand_budget_admin)
# class GrantAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Budget, site=grand_budget_admin)
# class Budget(admin.ModelAdmin):
#     pass
