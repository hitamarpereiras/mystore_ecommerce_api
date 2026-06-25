from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import HttpResponse

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOfOder

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfOder]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(customer__user=user)
