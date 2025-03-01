from django.urls import path
from .views import WalletCreateView,WalletUpdateView,WalletListView,WalletDeleteView

# urls do app wallet
urlpatterns = [
    path('', WalletListView.as_view(), name='wallet_list'),
    path('novo/', WalletCreateView.as_view(), name='wallet_create'),
    path('<int:pk>/editar/', WalletUpdateView.as_view(), name='wallet_update'),
    path('<int:pk>/deletar/', WalletDeleteView.as_view(), name='wallet_delete'),
]