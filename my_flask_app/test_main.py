import unittest
from unittest.mock import patch
from main import get_market_data, calculate_spread# Asumiendo que el código anterior está en un archivo llamado main.py

class TestApp(unittest.TestCase):
    @patch('main.requests.get')
    def test_get_market_data(self, mock_get):
        mock_get.return_value.json.return_value = {'ticker': {'max_bid': ['5000'], 'min_ask': ['6000']}}
        data = get_market_data('btc-clp')
        self.assertEqual(data, {'ticker': {'max_bid': ['5000'], 'min_ask': ['6000']}})

    def test_calculate_spread(self):
        data = {'ticker': {'max_bid': ['5000'], 'min_ask': ['6000']}}
        spread = calculate_spread(data)
        self.assertEqual(spread, 1000)

if __name__ == '__main__':
    unittest.main()