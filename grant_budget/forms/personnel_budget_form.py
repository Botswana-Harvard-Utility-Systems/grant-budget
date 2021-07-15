from django import forms
from ..models import PersonalBudget


class PersonnelBudgetForm(forms.ModelForm):
    class Meta:
        model = PersonalBudget
        fields = '__all__'

