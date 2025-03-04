
class User:
    def __init__(self, name, email, credit_card_number):
        self.__name = name
        self.__email = email
        self.__credit_card_number = credit_card_number
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_credit_card_number(self):
        return self.__credit_card_number