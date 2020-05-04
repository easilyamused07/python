import unittest
from city_function import city_and_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_function.py"""
    
    def test_city_and_country(self):
        """Do city and country like santiago chile work?"""
        test_formatted = city_and_country('santiago','chile')
        self.assertEqual(test_formatted,'Santiago, Chile')
    
    def test_city_and_country_and_population(self):
        """Do city, name and population work?"""
        test_formatted = city_and_country('santiago','chile',5000000)
        self.assertEqual(test_formatted,'Santiago, Chile - population 5000000')
unittest.main()
