import json
from urllib.parse import urljoin
import requests


class JustEatClient:
    """
    A client for interacting with the Just Eat API to retrieve restaurant data
    based on postal codes.
    """
    def __init__(self):
        self.BASE_URL = "https://uk.api.just-eat.io/restaurants/bypostcode/"

    def _get_restaurants_by_postal_code(self, postalcode: str) -> dict:
        """
        Retrieves restaurant data based on a given postal code.

        Args:
            postalcode (str): The postal code to search for restaurants.

        Returns:
            dict: A dictionary containing restaurant data.
        """

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          "AppleWebKit/537.36(KHTML, like Gecko) "
                          "Chrome/117.0.0.0 Safari/537.36"
        }
        url = urljoin(self.BASE_URL, postalcode)
        try:
            response = requests.get(url, headers=headers)
            restaurants_data = response.json()

        except requests.exceptions.RequestException as e:
            print("Network Error:", e)

        except requests.exceptions.HTTPError as e:
            print("HTTP Error:", e)

        return restaurants_data.get("Restaurants")

    def _parse_restaraunts(self, restaurant: dict) -> dict:
        """
        Parses a restaurant dictionary and extracts relevant information.

        Args:
            restaurant (dict): A dictionary representing a restaurant.

        Returns:
            dict: A dictionary with restaurant information.
        """
        return dict(
            name=restaurant.get("Name"),
            rating=restaurant.get("RatingAverage"),
            cuisines=[
                cuisine.get("Name") for cuisine in restaurant.get("Cuisines")
            ]
        )

    def from_postal_code(
            self,
            postalcode: str,
            write: bool = False
    ) -> list[dict]:
        """
        Retrieves a list of restaurants based on a postal code and optionally
        writes the data to a JSON file.

        Args:
            postalcode (str): The postal code to search for restaurants.
            write (bool, optional): Whether to write the data to a JSON file.

        Returns:
            list[dict]: A list of dictionaries containing restaurant
            information.
        """

        restaurants_data = self._get_restaurants_by_postal_code(postalcode)
        if not restaurants_data:
            print("There is no food delivery services in your area")
            return

        restaurants = [
            self._parse_restaraunts(restaurant) for restaurant in
            restaurants_data
        ]

        if write:
            self._write_to_file(restaurants, postalcode)

        return restaurants

    def _write_to_file(self, restaurants: list[dict], postalcode: str) -> None:
        """
        Writes restaurant data to a JSON file.

        Args:
            restaurants (list[dict]): A list of dictionaries containing
                restaurant information.
            postalcode (str): The postal code used to construct the file name.
        """
        filename = postalcode + "_restaurants.json"

        with open(filename, "w", encoding="utf-8") as restaurants_file:
            restaurants_file.write(
                json.dumps({"Restaurants": restaurants}, indent=4)
            )
