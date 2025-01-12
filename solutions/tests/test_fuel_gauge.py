import unittest

from ..fuel_gauge import fuel_gauge


class TestFuelGauge(unittest.TestCase):
    """Test cases for the fuel_gauge function."""

    def test_full(self):
        """Test cases where the percentage is 90%
        or more it should result in F."""
        self.assertEqual(fuel_gauge(90, 100), "F")
        self.assertEqual(fuel_gauge(100, 100), "F")
        self.assertEqual(fuel_gauge(97, 100), "F")

    def test_empty(self):
        """Test cases where the percentage is 10%
        or less it should result E."""
        self.assertEqual(fuel_gauge(10, 100), "E")
        self.assertEqual(fuel_gauge(0, 100), "E")
        self.assertEqual(fuel_gauge(2, 100), "E")

    def test_percentage(self):
        """Test cases where the result is between 90 and 10 it should be M."""
        self.assertEqual(fuel_gauge(71, 100), "M")
        self.assertEqual(fuel_gauge(23, 100), "M")
        self.assertEqual(fuel_gauge(10, 50), "M")

    def test_invalid_input(self):
        """Test cases for invalid inputs."""
        self.assertEqual(fuel_gauge(6, 0), "Invalid input")
        self.assertEqual(fuel_gauge(7, -1), "Invalid input")
