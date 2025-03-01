from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Wallet
from .forms import WalletCreate, WalletUpadate, WalletRead, WalletDelete

class WalletCreateView(FormView):
    template_name = 'Walletcreate.html'
    form_class = WalletCreate
    success_url = reverse_lazy('html_list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class WalletListView(ListView):
    model = Wallet
    template_name = 'list.html'
    context_object_name = 'Wallets'

class WalletUpdateView(UpdateView):
    model = Wallet
    fields = [ 'saldo','moeda']
    template_name = 'form.html'
    success_url = reverse_lazy('html_list')

class WalletDeleteView(DeleteView):
    model = Wallet
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('html_list')
