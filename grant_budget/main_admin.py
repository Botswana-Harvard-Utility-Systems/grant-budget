from django.contrib import admin


class GrandBudgetAdmin(admin.AdminSite):
    site_title = "Grant Budget Management System"
    site_header = site_title


grand_budget_admin = GrandBudgetAdmin(name='grand_budget_admin')
