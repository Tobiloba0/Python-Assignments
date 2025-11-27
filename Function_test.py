import unittest
from temperature_converter import temperature_checker

class TestTemperatureChecker(unittest.TestCase):

    def test_convert_celsius_to_farenheit(self):
        converted, unit, alert = temperature_checker(0, 'C')
        self.assertEqual(converted, 32)
        self.assertEqual(unit, 'F')
        self.assertEqual(alert, "Cold advisory")

    def test_convert_farenheit_to_celsius(self):
        converted, unit, alert = temperature_checker(212, 'F')
        self.assertAlmostEqual(converted, 100)
        self.assertEqual(unit, 'C')
        self.assertEqual(alert, "Heat alert")

    def test_normal_temperature(self):
        converted, unit, alert = temperature_checker(25, 'C')
        self.assertEqual(alert, "Normal temperature")

    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            temperature_checker(50, 'X')

if __name__ == "__main__":
    unittest.main()



#Testing for item discount

class TestApplyDiscount(unittest.TestCase):

    def test_save10_percent_discount(self):
        self.assertEqual(apply_discount("Yam", 100, "SAVE10"), 90)

    def test_half_off_the_price_discount(self):
        self.assertEqual(apply_discount("Bread", 200, "HALFOFF"), 100)

    def test_invalid_code_entry_from_users(self):
        self.assertEqual(apply_discount("Rice", 50, "NOTHING"), 50)

    def test_lowercase_letters_code(self):
        self.assertEqual(apply_discount("Hat", 100, "save10"), 90)

    def test_zero_price(self):
        self.assertEqual(apply_discount("Free item", 0, "SAVE10"), 0)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            apply_discount("Laptop", -20, "SAVE10")

if __name__ == "__main__":
    unittest.main()

