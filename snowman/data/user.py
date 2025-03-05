
class User:
    def __init__(self, name, email, credit_card_number, favorite_hobby):
        self._name = name
        self._email = email
        self._credit_card_number = credit_card_number
        self._favorite_hobby = favorite_hobby
    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_credit_card_number(self):
        return self._credit_card_number

    def favorite_hobby(self):
        return self._favorite_hobby