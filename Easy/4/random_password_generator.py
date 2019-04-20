import random
import string


def main():
    num_passwords = get_number_of_passwords()
    password_list = list()
    for _ in range(0, num_passwords):
        password = str()
        for _ in range(0, random.randint(10, 20)):
            password += random.choice(string.ascii_letters + string.digits)
        password_list.append(password)

    for x in password_list:
        print(x)


def get_number_of_passwords():
    while True:
        num_passwords = input('How many passwords do you want to generate? ')
        if num_passwords.isdigit():
            return int(num_passwords)


if __name__ == '__main__':
    main()