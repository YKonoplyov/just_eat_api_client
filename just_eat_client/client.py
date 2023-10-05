class JustEatClient:
    """
    A client for interacting with the Just Eat API to retrieve restaurant data
    based on postal codes.
    """
    def __init__(self):
        self.BASE_URL = "https://uk.api.just-eat.io/restaurants/bypostcode/"
