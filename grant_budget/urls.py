from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from .admin_site import grant_budget_admin

app_name = 'grant_budget'

urlpatterns = [
    path('administrator/', grant_budget_admin.urls),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='administrator/'), name='home_url')
]
