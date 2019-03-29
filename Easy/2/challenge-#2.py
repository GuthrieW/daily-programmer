def main():
    print("This program calculates an object's force (F), mass (M) or acceleration given both of the"
          "other two variables.")
    while True:
        calculate = raw_input("What would you like to calculate: F, M or A? ")
        if calculate.lower() == "f" or calculate.lower() == "m" or calculate.lower() == "a":
            break
    if calculate == "F":
        acceleration = get_numerical_input("What is the object's rate of acceleration in meters per second squared? ")
        mass = get_numerical_input("What is the mass of the object in kilograms? ")
        print("The amount of force the object is exerting is {} Newtons.".format(mass * acceleration))
    elif calculate == "M":
        acceleration = get_numerical_input("What is the object's rate of acceleration in meters per second squared? ")
        force = get_numerical_input("What is the amount of force the object is exerting in Newtons? ")
        print("The object's mass is {} kilograms.".format(force / acceleration))
    elif calculate == "A":
        mass = get_numerical_input("What is the mass of the object in kilograms? ")
        force = get_numerical_input("What is the amount of force the object is exerting in Newtons? ")
        print("The object is accelerating at a rate of {} meters per second squared.".format(force / mass))
    else:
        print("This is awkward. Calculate was equal to {}, but it should be one of F, M, or A...".format(calculate))


def get_numerical_input(question):
    while True:
        value = raw_input(question)
        if value.isdigit():
            break

    return int(value)


if __name__ == '__main__':
    main()