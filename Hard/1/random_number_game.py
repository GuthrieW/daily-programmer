def main():
	print("Choose a number between 1 and 100. I'm going to start with 50 as my guess.")
	current_guess = 50
	current_lowest = 1
	current_highest = 101

	while True:
		answer = check_guess(current_guess)
		if answer == "correct":
			print("I win!")
			exit(0)
		elif answer == "higher":
			current_lowest = current_guess
			current_guess = int((current_guess + current_highest) / 2)
		elif answer == "lower":
			current_highest = current_guess
			current_guess = int((current_guess + current_lowest) / 2)
		else:
			print("This is awkward... You told me my guess was {}.\nI'm not sure what to do so I'm going to stop playing.".format(answer))
			exit(1)


def check_guess(current_guess):
	while True:
		answer = input("My current guess is {}. Higher, lower, or correct? ".format(current_guess)).lower()
		if answer == "higher" or answer == "lower" or answer == "correct":
			break

	return answer


if __name__ == '__main__':
	main()