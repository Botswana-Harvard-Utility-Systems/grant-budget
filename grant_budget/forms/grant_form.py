from django import forms
from ..models import Grant


class GrantForm(forms.ModelForm):

    class Meta:
        model = Grant
        fields = '__all__'
