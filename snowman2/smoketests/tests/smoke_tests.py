import json
from unittest import TestCase
import requests
import os
from pprint import pprint
class SmokeTests(TestCase):
    def test_get_user(self):
        url = f"{os.environ['SNOWMAN_URL']}/snowman/user/all"
        print(url)
        response = requests.get(url)
        pprint(response.json())
    def test_add_user(self):
        url = f"{os.environ['SNOWMAN_URL']}/snowman/user/add"
        data = {"name" : "JohnTravolta", "email":"johnny5speed@gmail.com"}
        print(url)
        response = requests.post(url, params=data)
        pprint(response)
