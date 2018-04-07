import unittest
from details_functions import get_details

class DetailsTestCase(unittest.TestCase):
    def test_city_country(self):
        details = get_details('chicago', 'USA')
        self.assertEqual(details, 'Chicago, Usa')
    
    def test_city_coutry_pop(self):
        details = get_details('delhi', 'India', '1 billion')
        self.assertEqual(details, 'Delhi, India, 1 Billion')

unittest.main()
