<<<<<<< HEAD
from rest_framework import generics
from django.contrib.auth.models import User

from economy_partner.models import Account, Transaction, Category
from economy_partner.serializers import (
    AccountSerializer, TransactionSerializer, CategorySerializer)

# Account API Views
class AccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        return super().perform_create(serializer)


class AccountDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # lookup_field = 'pk'


# Category API Views
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # lookup_field = 'pk'


# Trasaction API Views
class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # lookup_field = 'pk'
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> main
