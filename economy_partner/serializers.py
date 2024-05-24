from rest_framework import serializers

from . models import Account, Category, Transaction

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'account_type',
            'name',
            'initial_balance',
            'balance',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            'id',
            'account',
            'date',
            'transaction_type',
            'ammount',
            'category',
            'description',
        ]