from django import forms
from car.models.contract import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"