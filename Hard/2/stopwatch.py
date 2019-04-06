import time


def main():
    while True:
        print("Press enter to start the timer")
        print("You may enter Q at any time to close the timer")
        check_for_quit = input().lower()
        if check_for_quit == "q":
            exit(0)
        print("To put your lap time type L.\nTo stop the timer type S.\nTo close the timer type Q")

        start_time = int(time.time())
        current_lap_time = start_time

        laps = []
        while True:
            command = get_command()
            if command == "l":
                lap_last_time = current_lap_time
                current_lap_time = int(time.time())
                lap_elapsed_time = current_lap_time - lap_last_time
                laps.append(lap_elapsed_time)
                print("Lap time: {} second(s)".format(lap_elapsed_time))
            elif command == "s":
                stop_time = int(time.time()) - start_time
                break
            elif command == "q":
                exit(0)

        output_string = ""
        if len(laps) > 0:
            output_string += "Your lap time(s) were:\n"
            for lap_number, lap in enumerate(laps):
                output_string += "Lap {}: {} second(s)\n".format(lap_number + 1, lap)

        output_string += "Total elapsed time: {} second(s).\n".format(stop_time)

        save_to_file(output_string)
        print("\n" + output_string)


def save_to_file(string_to_save):
    timer_output = open("timer_output.txt", "w")
    timer_output.write(string_to_save)
    timer_output.close()


def get_command():
    while True:
        command = input().lower()
        if command == "l" or command == "s" or command == "q":
            return command


if __name__ == '__main__':
    main()