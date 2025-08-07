from random import randint
from datetime import datetime
from datetime import time
from datetime import timedelta

today = datetime.now()


def words_to_slug(words):
    slug_dict = [
        "a",
        "b",
        "v",
        "g",
        "d",
        "e",
        "zh",
        "z",
        "i",
        "y",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "r",
        "s",
        "t",
        "u",
        "f",
        "h",
        "c",
        "ch",
        "sh",
        "shch",
        "",
        "y",
        "",
        "e",
        "yu",
        "ya",
    ]

    start_index = ord("а")
    slug = ""
    for w in words.lower():
        if "а" <= w <= "я":
            slug += slug_dict[ord(w) - start_index]
        elif w == "ё":
            slug += "yo"
        elif w in " !?;:.,":
            slug += "-"
        elif w in '"':
            slug += "-"
        else:
            slug += w
    while slug.count("--"):
        slug = slug.replace("--", "-")
    suffix1 = chr(randint(97, 122))
    suffix2 = chr(randint(97, 122))
    slug = slug + suffix1 + suffix2
    return slug


def appoitment_slots(worker=None, pre_entry_days=30, day_of_week=3, start_time=(9, 0), end_time=(14, 0),
                     appointment_duration=30):
    # woker = woker

    for i in range(pre_entry_days):

        day = today + timedelta(days=i)
        if day.weekday() == day_of_week:
            h1, m1 = start_time
            h2, m2 = end_time
            s_time = datetime(day.year, day.month, day.day, h1, m1)
            e_time = datetime(day.year, day.month, day.day, h2, m2)
            while s_time < e_time:
                print(s_time)
                s_time += timedelta(minutes=appointment_duration)


if __name__ == "__main__":
    appoitment_slots()
