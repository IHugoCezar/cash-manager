from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Wallet
from .forms import WalletCreate
from decimal import Decimal
import requests
import os

#criacao do objeto carteira e seus derivados
class WalletCreateView(FormView):
    template_name = 'wallets/form.html'
    form_class = WalletCreate
    success_url = reverse_lazy('wallet_list')
    
    # salva os dados da variavel wallet sem enviar ao banco/ adciona o user manualmente
    def form_valid(self, form): 
        wallet = form.save(commit=False)
        wallet.user = self.request.user
        wallet.save()
        return super().form_valid(form)
    
# vizualizar os dados com templates 
class WalletListView(ListView):
    model = Wallet
    template_name = 'wallets/list.html'
    context_object_name = 'wallets'

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)
    
    # dados convertidos para o hmtl
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        api_url = "https://data.fixer.io/api/latest"
        access_key = os.environ.get("FIXER_API_KEY", "")

        converted_wallets = []
        for wallet in context['wallets']:
            base_currency = wallet.moeda 
            
            params = {"access_key": access_key, "base": base_currency}
            response = requests.get(api_url, params=params)
            
            try:
                exchange_rates = response.json().get("rates", {})
            except Exception:
                exchange_rates = {} 
            
            # Conversor das moedas pra decimal
            rate_usd = Decimal(str(exchange_rates.get("USD", 1)))
            rate_eur = Decimal(str(exchange_rates.get("EUR", 1)))
            rate_brl = Decimal(str(exchange_rates.get("BRL", 1)))

            # conversor para outras moedas
            saldo_usd = wallet.saldo * rate_usd
            saldo_eur = wallet.saldo * rate_eur
            saldo_brl = wallet.saldo * rate_brl

            converted_wallets.append({
                "user": wallet.user,
                "saldo_original": wallet.saldo,
                "moeda": base_currency,
                "saldo_usd": saldo_usd.quantize(Decimal('0.01')), 
                "saldo_eur": saldo_eur.quantize(Decimal('0.01')),
                "saldo_brl": saldo_brl.quantize(Decimal('0.01')),
            })

        context['converted_wallets'] = converted_wallets
        return context
    
    # filtro das carteiras wallets autenticadas do usuario atual
class WalletUpdateView(UpdateView):
    model = Wallet
    fields = [ 'saldo','moeda']
    template_name = 'wallets/form.html'
    success_url = reverse_lazy('wallet_list')

class WalletDeleteView(DeleteView):
    model = Wallet
    template_name = 'wallets/confirm_delete.html'
    success_url = reverse_lazy('wallet_list')
