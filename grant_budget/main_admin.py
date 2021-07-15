from django.contrib.admin import AdminSite

class GrandBudgetAdminSite(AdminSite):
    pass


grand_budget_admin = GrandBudgetAdminSite(name='grant_budget_admin')