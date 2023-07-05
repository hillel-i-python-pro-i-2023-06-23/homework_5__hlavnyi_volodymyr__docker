from faker import Faker


# Return string with - fake first name
def get_random_first_name():
    faker = Faker()
    random_name = faker.first_name()
    return random_name


def get_random_last_name():
    faker = Faker()
    random_name = faker.last_name()
    return random_name


def get_random_mobile_phone():
    faker = Faker()
    random_phone = faker.phone_number()
    return random_phone


# print Hi and same fake first Name
def print_random_name_greetings():
    first_name = get_random_first_name()
    last_name = get_random_last_name()
    phone = get_random_mobile_phone()
    print(f"Hi {first_name} {last_name}! My mobile is {phone}.")


# main procedure
# wo any parameter
def main():
    print_random_name_greetings()
    print_random_name_greetings()
