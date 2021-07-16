from django.apps import AppConfig


class GrantBudgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grant_budget'
    app_label = 'grant_budget'
    admin_site_name = 'grand_budget_admin'
    identifier_pattern = None
