from unittest import TestCase
from calculate_pay import calculate_pay


class TestCalculatePay(TestCase):
    def test_calculate_pay_wage_low_bound(self):
        self.assertEqual(0, calculate_pay(20, 0))

    def test_calculate_pay_hours_low_bound(self):
        self.assertEqual(0, calculate_pay(0, 10))

    def test_calculate_pay_over_40(self):
        self.assertEqual(500, calculate_pay(45, 10))
