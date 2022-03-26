import unittest
from datetime import date

from tire.carrigantire import CarriganBattery


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        num1=0.9
        num2=0.1
        num3=0.2
        num4=0.2
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        num1=0.1
        num2=0.1
        num3=0.2
        num4=0.2
        self.assertFalse(tire.needs_service())
