secret = 25
chances = 5

while chances > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct! You guessed the number.")
        break

    elif guess < secret:
        print("Higher")

    else:
        print("Lower")

    chances -= 1
    print("Chances left:", chances)

if chances == 0:
    print("Game Over! The number was", secret)