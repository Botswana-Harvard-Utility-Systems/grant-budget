from django import forms
from ..models import Budget


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'

