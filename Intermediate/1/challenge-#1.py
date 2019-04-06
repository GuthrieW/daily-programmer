SHOW_EVENTS = 1
ADD_EVENT = 2
REMOVE_EVENT = 3
EDIT_EVENT = 4
HELP = 5
EXIT = 6
EDIT_EVENT_NAME = 1
EDIT_EVENT_TIME_AND_LENGTH = 2
EMPTY_TIME_SLOT = "EMPTY"


def main():
    events = [EMPTY_TIME_SLOT for x in range(24)]

    while True:
        action = print_menu()
        if action == SHOW_EVENTS:
            show_events(events)
        elif action == ADD_EVENT:
            event_to_add = raw_input("What is the name of the even you would like to add?\n")
            events = add_event(events, event_to_add)
        elif action == REMOVE_EVENT:
            event_to_remove = raw_input("What event would you like to remove?\n")
            events = remove_event(events, event_to_remove)
        elif action == EDIT_EVENT:
            events = edit_event(events)
        elif action == HELP:
            help()
        elif action == EXIT:
            exit(0)
        print("=========================\n\n")


def show_events(events):
    counter = 0
    for event in events:
        print("{}:00 - {}".format(counter, event))
        counter += 1


def add_event(events, event_to_add):
    while True:
        start_time = input("When does the event start?\n")
        hours = input("How many hours will the event last?\n")
        if start_time.isdigit() and \
                hours.isdigit() and \
                -1 < int(start_time) < 24 and \
                0 < int(hours) < 24 and \
                int(start_time) + int(hours) < 24:
            break

    for hour in range(int(hours)):
        events[hour + int(start_time)] = event_to_add
    return events


def remove_event(events, event_to_remove):
    event_found = False
    for hour in range(24):
        if events[hour] == event_to_remove:
            event_found = True
            events[hour] = EMPTY_TIME_SLOT

    if not event_found:
        print("Could not remove event: EVENT_NAME_NOT_FOUND")
    return events


def edit_event(events):
    event_to_edit = raw_input("What event would you like to edit?\n")
    while True:
        print("What would you like to edit?")
        print("1. Event name")
        print("2. Event time and length")
        action = input()
        if action.isdigit() and 0 < int(action) < 3:
            break

    if int(action) == EDIT_EVENT_NAME:
        new_event_name = input("What would you like to rename the event to?\n")
        for hour in range(24):
            if events[hour] == event_to_edit:
                events[hour] = new_event_name
    elif int(action) == EDIT_EVENT_TIME_AND_LENGTH:
        remove_event(events, event_to_edit)
        add_event(events, event_to_edit)

    return events


def help():
    print("This program the events of a day by hour. You can add, remove or edit events.\n"
          "Event times cannot conflict with each other. ")


def print_menu():
    while True:
        print("What would you like to do?")
        print("1. Show day's events")
        print("2. Add event")
        print("3. Remove event")
        print("4. Edit event")
        print("5. Help")
        print("6. Exit")

        action = input()
        if action.isdigit():
            if 0 < int(action) < 7:
                break

    return int(action)


if __name__ == '__main__':
    main()