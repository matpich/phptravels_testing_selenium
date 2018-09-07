import random

class User():
    first_name="John"
    last_name="Doe"
    mobile="123456789"
    email="john{}.doe@doe.doe".format(random.randint(0,9999))
    password="qwerty"
    confirm_password="qwerty"