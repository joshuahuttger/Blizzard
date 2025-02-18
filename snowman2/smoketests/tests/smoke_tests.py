from unittest import TestCase
import requests
import os

class SmokeTests(TestCase):
    def test_create_user(self):
        request_url = f"{os.environ['SNOWMAN_URL']}/createUser?first_name=testFirstName&last_name=testLastName"
        print(f"Request = {request_url}")
        response = requests.get(request_url)
        response_json = response.json()
        del response_json['id']
        self.assertEqual(response_json, {
            "firstName": "testFirstName",
            "lastName": "testLastName"
        })
