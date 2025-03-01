from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    """ Modelo da carteira """
    #  on_delete=models.CASCADE: deleta carteiras do usuario removido, related_name="wallets": serve para referenciar as carteiras do usuario
    saldo = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    moeda = models.CharField(max_length=3, default="EUR")  

    def __str__(self):
        return f"{self.user.username} - {self.moeda} {self.saldo}"
