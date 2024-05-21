from rest_framework import serializers

from . models import Account, Category, Transaction

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'account_type',
            'name',
            'balance',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]

class TransactionSerializer(serializers.ModelSerializer):
    account = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

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
        
    def get_account(self, obj):
        return str(obj.account)
    
    def get_category(self, obj):
        return str(obj.category)