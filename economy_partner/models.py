<<<<<<< HEAD
from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.dispatch import receiver
from django.db. models.signals import post_delete


class Account(models.Model):
    ACCOUNT_TYPES = [
        ('RESERVA', 'Reserva'),
        ('CONTA', 'Conta'),
        ('INVESTIMENTO', 'Investimento'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    initial_balance = models.DecimalField(max_digits=15, decimal_places=2,
                                          default=0.00,)
    balance = models.DecimalField(max_digits=15, decimal_places=2,
                                  default=initial_balance, editable=False)

    def update_balance(self):
        income_sum = self.transactions.filter(
                transaction_type='RENDIMENTO').aggregate(
                total=models.Sum('ammount'))['total'] or Decimal('0.00')
        print(income_sum)
        expense_sum = self.transactions.filter(
                transaction_type='GASTO').aggregate(
                total=models.Sum('ammount'))['total'] or Decimal('0.00')    
        total_balance = self.initial_balance + income_sum - expense_sum
        self.balance = total_balance
        self.save()

    def __str__(self):
        return f'{self.account_type.capitalize()}: {self.name}'
    

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

    account = models.ForeignKey(
            Account,related_name='transactions', on_delete=models.CASCADE)
    transaction_type = models.CharField(
            max_length=20, choices=TRANSACTION_TYPES)
    date = models.DateField()
    ammount = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(
            Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=140 ,blank=True)

    def save(self, *args, **kwargs):
        self.account.update_balance()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.date:%d-%m-%Y} | {self.transaction_type}: R$ {self.ammount}'

@receiver(post_delete, sender=Transaction)
def update_account_balance_on_delete(sender, instance, **kwargs):
    instance.account.update_balance()
=======
from django.db import models

# Create your models here.
>>>>>>> main
