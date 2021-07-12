from django.contrib import admin


class GrandBudgetAdmin(admin.AdminSite):
    site_title = "Grant Budget Management System"


grand_budget_admin = GrandBudgetAdmin(name='grand_budget_admin')
