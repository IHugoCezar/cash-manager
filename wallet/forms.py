from django import forms
from .models import Wallet

class WalletCreate(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['saldo','moeda']

class WalletRead(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['saldo','moeda']
        # Cria o html e comunica com o banco
        widgets = {
            'user': forms.TextInput(attrs={'readonly': True}),
            'saldo': forms.TextInput(attrs={'readonly': True}),
            'moeda': forms.TextInput(attrs={'readonly': True}),
        }
        
class WalletUpadate(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['saldo','moeda']
        
class WalletDelete(forms.ModelForm):
    class Meta:
        confirm = forms.BooleanField(label="Deseja deletar sua carteira?")

    
