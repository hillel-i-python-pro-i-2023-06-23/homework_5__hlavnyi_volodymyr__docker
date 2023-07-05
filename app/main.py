from faker import Faker


# Return string with - fake first name
def get_random_name_4_greetings():
    faker = Faker()
    random_first_name = faker.first_name()
    return random_first_name


# print Hi and same fake first Name
def print_random_name_greetings():
    print(f"Hi {get_random_name_4_greetings()}!")


# main procedure
# wo any parameter
def main():
    print_random_name_greetings()
