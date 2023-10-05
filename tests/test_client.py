import unittest
from unittest.mock import patch, Mock
from main import validate_postalcode
from just_eat_client import JustEatClient


class TestJustEatClient(unittest.TestCase):

    def test_get_restaurants_by_postal_code(self):
        response_data = {
            "Restaurants": [
                {"some_interesting_data": "really interesting"},
                {"also, very valuable": "really valuable"},
            ]
        }
        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = response_data
            mock_response.status_code = 200
            mock_get.return_value = mock_response

            client = JustEatClient()
            restaurants_data = client._get_restaurants_by_postal_code(
                "SW1A 1AA"
            )

            self.assertEqual(
                restaurants_data, response_data.get("Restaurants")
            )

    def test_parse_restaurants(self):
        restaurant_data = {
            "Name": "Restaurant Name",
            "RatingAverage": 4.5,
            "Cuisines": [{"Name": "Italian"}, {"Name": "Pizza"}]
        }
        client = JustEatClient()
        parsed_restaurant = client._parse_restaraunts(restaurant_data)

        expected_result = {
            "name": "Restaurant Name",
            "rating": 4.5,
            "cuisines": ["Italian", "Pizza"]
        }

        self.assertEqual(parsed_restaurant, expected_result)

    def test_validate_postalcode(self):
        valid_postal_codes = ["SW1A 1AA", "EC1A 1BB", "W1A 0AX", "GIR 0AA"]
        for postal_code in valid_postal_codes:
            self.assertTrue(validate_postalcode(postal_code))

        invalid_postal_codes = ["12345", "AB12 CD", "X1Y 2Z3"]
        for postal_code in invalid_postal_codes:
            self.assertFalse(validate_postalcode(postal_code))
