import requests
import os
import unittest


class SnowmanSignupSmokeTests(unittest.TestCase):
    def createUserTest(self):
        request_url = f"{os.environ['SNOWMAN_URL']}/createUser?first_name=testFirstName&last_name=testLastName"
        print(f"Request = {request_url}")
        response = requests.get(request_url)
        response_json = response.json()
        del response_json['id']
        self.assertEqual(response.json(),{
            "firstName":"testFirstNames",
            "lastName":"testLastName"
        })

if __name__ == '__main__':
    unittest.main()



