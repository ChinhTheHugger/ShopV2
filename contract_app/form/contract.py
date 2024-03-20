from django import forms
from contract_app.model.contract import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"