from django.contrib.auth.models import User # modelo de usuario do django
from django.db import models


class Wallet(models.Model):
    """ Modelo da carteira """
    #  on_delete=models.CASCADE: deleta carteiras do usuario removido, related_name="wallets": serve para referenciar as carteiras do usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wallets") 
    saldo = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    moeda = models.CharField(max_length=3, default="BRL")  

    def deposit(self, amount):
        """Deposito para a carteira"""
        self.saldo += amount
        self.save()

    def withdraw(self, amount):
        """Remover da carteira"""
        if self.saldo >= amount:
            self.saldo -= amount
            self.save()
            return True
        return False

    def __str__(self):
        return f"{self.user.username} - {self.moeda} {self.saldo}"
