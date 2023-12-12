from django.test import TestCase, Client
from django.urls import reverse
from .models import Stock, Order
import json


class TradingSystemTest(TestCase):
    def setUp(self):
        # Create some test data
        self.stock1 = Stock.objects.create(name='AAPL', price=150.0)
        self.stock2 = Stock.objects.create(name='GOOGL', price=2500.0)

    def test_stock_list(self):
        response = self.client.get(reverse('stock-list'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)  # Assuming two stocks were created in setUp

    def test_order_creation(self):
        order_data = {
            'stock': self.stock1.id,
            'quantity': 10,
            'price': 155.0,
        }
        response = self.client.post(reverse('order-list-create'), data=json.dumps(order_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)  # Created status
        self.assertEqual(Order.objects.count(), 1)

    def test_portfolio_value(self):
        # Create an order for stock1
        Order.objects.create(stock=self.stock1, quantity=5, price=150.0)

        response = self.client.get(reverse('portfolio-value'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['portfolio_value'], 5 * 150.0)

    def test_portfolio_value_empty_portfolio(self):
        response = self.client.get(reverse('portfolio-value'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['portfolio_value'], 0.0)

    def test_portfolio_value_single_order(self):
        Order.objects.create(stock=self.stock1, quantity=5, price=160.0)
        response = self.client.get(reverse('portfolio-value'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        expected_value = 5 * 160.0
        self.assertAlmostEqual(data['portfolio_value'], expected_value, delta=0.001)

    def test_portfolio_value_multiple_orders(self):
        Order.objects.create(stock=self.stock1, quantity=5, price=160.0)
        Order.objects.create(stock=self.stock2, quantity=2, price=2600.0)
        response = self.client.get(reverse('portfolio-value'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        expected_value = (5 * 160.0) + (2 * 2600.0)
        self.assertAlmostEqual(data['portfolio_value'], expected_value, delta=0.001)

    def test_portfolio_value_zero_quantity_order(self):
        Order.objects.create(stock=self.stock1, quantity=0, price=160.0)
        response = self.client.get(reverse('portfolio-value'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['portfolio_value'], 0.0)

    def test_portfolio_value_negative_quantity_order(self):
        Order.objects.create(stock=self.stock1, quantity=-3, price=160.0)
        response = self.client.get(reverse('portfolio-value'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['portfolio_value'], 0.0)  # Negative quantity should be ignored

    def test_portfolio_value_negative_price_order(self):
        Order.objects.create(stock=self.stock1, quantity=2, price=-160.0)
        response = self.client.get(reverse('portfolio-value'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['portfolio_value'], 0.0)