print("Welcome to the word guessing game , you get 5 chances to guess the secret word")
secret_word = "apple"
guess_count = 0
guess_limit = 5


while guess_count < guess_limit:
    guess= input("Enter your guess: ")
    if guess == secret_word :
        print("You guessed the word correctly")
        break
    guess_count = guess_count + 1

    if guess_count >= guess_limit:
        print("You ran out of guesses")
        break