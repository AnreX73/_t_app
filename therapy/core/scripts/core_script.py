import random
from faker import Faker

from core.models import User, Bid

from core.utils import words_to_slug

fake = Faker("ru_RU")


def run():












    # BIDS IS IT CHILD
    # bids = Bid.objects.all()

    # for bid in bids:
    #     bid.is_child_bid = random.choice([True, False])
    #     bid.save()

    # CREATE BIDS
    # customers = User.objects.filter(role=3)
    # workers = User.objects.filter(role=2)
    # for customer in customers:
    #     customer = customer
    #     worker = random.choice(workers)
    #     date = fake.date_between(start_date="today", end_date="+30d")
    #     time = fake.time_object()
    #     Bid.objects.create(customer=customer, worker=worker, date=date, time=time)
    
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
