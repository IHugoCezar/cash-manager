from django import forms
from .models import Wallet

 # formulario criar objeto do modelo para a comunicacao banco
class WalletCreate(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['saldo','moeda']


    
