from django.urls import path
from .main_admin import grand_budget_admin

app_name = 'grant_budget'
app_label = 'grant_budget'

urlpatterns = [
    path('', grand_budget_admin.urls)
]
