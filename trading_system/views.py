from .models import Stock, Order
from .serializers import StockSerializer, OrderSerializer
from django.db.models import F, ExpressionWrapper, fields
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view



class StockList(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['GET'])
def portfolio_value(request):
    # Exclude orders with negative quantities or negative prices
    orders = Order.objects.filter(quantity__gt=0, stock__price__gt=0)

    # Debug prints
    for order in orders:
        print(f"Order: Stock - {order.stock.name}, Quantity - {order.quantity}, Price - {order.stock.price}")
    total_value = sum(order.quantity * order.price for order in orders)
    if total_value < 0:
        total_value = 0
    return Response({'portfolio_value': total_value})