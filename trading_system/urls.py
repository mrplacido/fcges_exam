from django.urls import path
from .views import StockList, OrderListCreate, portfolio_value

urlpatterns = [
    path('stocks/', StockList.as_view(), name='stock-list'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('portfolio_value/', portfolio_value, name='portfolio-value'),
]