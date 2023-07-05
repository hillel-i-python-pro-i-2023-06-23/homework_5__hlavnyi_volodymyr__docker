from faker import Faker


def get_random_name_4_greetings():
    faker = Faker()
    random_first_name = faker.first_name()
    return random_first_name


def print_random_name_greetings():
    print(f"Hi {get_random_name_4_greetings()}!")


def main():
    print_random_name_greetings()
