import random


def main():
    user_health, user_attack, = 20
    enemy_name, enemy_health, enemy_attack = get_random_enemy()
    print("You're being attacked by a {}!".format(enemy_name))
    while True:
        command = get_command()
        if command == "a":
            enemy_health -= (user_attack * random.randint(1, user_attack)) / 10
        elif command == "r":
            if random.randint(1, 10) > 8:
                print("You ran from the {}.".format(enemy_name))
        elif command == "h":
            user_health += 10
            if user_health > 20:
                user_health = 20
        if enemy_health <= 0:
            print("You win!")
            exit(0)

        user_health -= (enemy_attack * random.randint(1, enemy_attack)) / 10
        if user_health <= 0:
            print("You lose.")
            exit(0)
            

def get_command():
    while True:
        command = input("What would you like to do?\nAttack - a\nRun - r\nHeal - h").lower()
        if command == "a" or command == "r" or command == "h":
            return command


def get_random_enemy():
    random_line = random.choice(open("./enemies.txt", "r").readlines())
    return random_line.split(",")


if __name__ == '__main__':
    main()