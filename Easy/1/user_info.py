def main():
    name = input("What is your name? ")
    age = input("How old are you? ")
    reddit_username = input("What is your reddit username? ")
    save_to_file(name, age, reddit_username)
    print("your name is {}, you are {} years old, and your username is {}".format(name, age, reddit_username))


def save_to_file(name, age, username):
    file = open("./user_information.txt", "w")
    file.write(name + "\n" + age + "\n" + username)
    file.close()


if __name__ == '__main__':
    main()