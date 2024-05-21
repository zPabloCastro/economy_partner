from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('RESERVA', 'Reserva'),
        ('CONTA', 'Conta'),
        ('INVESTIMENTO', 'Investimento'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('RENDIMENTO', 'Rendimento'),
        ('GASTO', 'Gasto')
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20,choices=TRANSACTION_TYPES)
    date = models.DateField()
    ammount = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(
            Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=140 ,blank=True)

    def __str__(self):
        return f'{self.date} | {self.transaction_type}: R$ {self.ammount}'