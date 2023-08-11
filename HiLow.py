low = 1
high = 1000

print("Please think of a number between {0} and {1}".format(low, high))
input("Press ENTER to start")

guesses = 1
while True:
    print("\tGuessing in the range of {0} and {1}. ".format(low, high))
    guess = low + (high - low) // 2
    guesses += 1
    high_low = input("My guess is {0}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {0} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, or c. ")




