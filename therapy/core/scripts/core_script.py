import random
from faker import Faker

from core.models import User

from core.utils import words_to_slug

fake = Faker("ru_RU")


# def run():
    # CREATE USERS

    # for _ in range(20):
    #     first_name_ = (fake.first_name())
    #     username_ = words_to_slug(first_name_)
    #     sex_ = (random.randint(1, 2))
    #     User.objects.create_user(
    #         username=username_,
    #         first_name=first_name_,
    #         password="l010800l",
    #         email=username_ + "@test.com",
    #         sex=sex_,
    #         role=3,
    #         phone=fake.phone_number(),
    #     )
