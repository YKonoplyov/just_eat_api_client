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
        print(restaurants_data)
        return restaurants_data.get("Restaurants")

    def from_postal_code(
            self,
            postalcode: str,
            write: bool = False
    ) -> list[dict]:
        """
        Retrieves a list of restaurants based on a postal code

        Args:
            postalcode (str): The postal code to search for restaurants.

        Returns:
            list[dict]: A list of dictionaries containing restaurant
            information.
        """

        restaurants_data = self._get_restaurants_by_postal_code(postalcode)
        if not restaurants_data:
            print("There is no food delivery services in your area")
            return
