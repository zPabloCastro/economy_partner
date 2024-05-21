from rest_framework import generics

from economy_partner.models import Transaction
from economy_partner.serializers import TransactionSerializer

class TransactionListAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer