import random


def main():
    user_health = 20
    user_attack = 20
    enemy_name, enemy_health, enemy_attack = get_random_enemy()
    print("You're being attacked by a {}!".format(enemy_name))
    while True:
        command = get_command()
        if command == "a":
            attack_amount = random.randint(1, user_attack)
            print("You did {} points of damage.".format(attack_amount))
            enemy_health -= attack_amount
        elif command == "r":
            if random.randint(1, 10) > 8:
                print("You ran from the {}.".format(enemy_name))
                exit(0)
            else:
                print("You failed to get away")
        elif command == "h":
            user_health += 10
            if user_health > 20:
                user_health = 20

        print("The enemy's health is now {}".format(enemy_health))
        if enemy_health <= 0:
            print("You win!")
            exit(0)

        print("The enemy attacks!")
        attack_amount = random.randint(1, enemy_attack)
        print("The enemy did {} points of damage.".format(attack_amount))
        user_health -= attack_amount
        print("Your health is now {}". format(int(user_health)))

        if user_health <= 0:
            print("You lose.")
            exit(0)


def get_command():
    while True:
        command = input("What would you like to do?\nAttack - a\nRun - r\nHeal - h\n").lower()
        if command == "a" or command == "r" or command == "h":
            return command


def get_random_enemy():
    random_line = random.choice(open("./enemies.txt", "r").readlines())
    name, health, attack = random_line.split(",")
    return name, int(health), int(attack)


if __name__ == '__main__':
    main()