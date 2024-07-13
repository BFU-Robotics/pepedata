
import requests
import json


class PlankaAPIClient:
    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.username = username
        self.password = password
        self.auth_token = None

        self.authenticate()

    def __repr__(self):
        return f"<{type(self).__name__}:\n\tBase URL: {self.url}\n\tLogin User: {self.username}\n\tLogin Pass: {self.password}\n\tAPI Token: {self.auth_token}\n>"

    def deauthenticate(self) -> bool:
        try:
            self.request("DELETE", "/api/access-tokens/me")
            self.auth_token = None
            return True
        except:
            raise InvalidToken(
                f"No active access token assigned to this instance\n{self.__repr__()}")

    def authenticate(self) -> bool:
        try:
            request = requests.post(f"{self.url}/api/access-tokens", data={
                                    'emailOrUsername': self.username, 'password': self.password})
            self.auth_token = request.json()['item']
            print(request.json(), flush=True)
            if not self.auth_token:
                raise InvalidToken(
                    f"Invalid API credentials\n{self.__repr__()}")
            return True
        except:
            raise InvalidToken(f"Invalid API credentials\n{self.__repr__()}")

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
        }

    def get_projects(self):
        print(self.get_headers(), flush=True)
        request = requests.get(
            f"{self.url}/api/projects", headers=self.get_headers())

        return request.json()['items']

    def get_boards(self):
        request = requests.get(
            f"{self.url}/api/projects", headers=self.get_headers())

        return request.json()['included']['boards']

    def get_cards(self, board_id: str):
        # Implement the actual API call to get cards
        pass


class InvalidToken(Exception):
    """General Error for invalid API inputs
    """
    pass
