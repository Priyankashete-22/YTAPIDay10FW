import requests


class APIClient:
    base_url = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
        }

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def put(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, headers=self.headers, json=data)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, headers=self.headers)
        return response