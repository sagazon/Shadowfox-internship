import random

words_and_hints = {"python":"A popular programming langauge",
                   "elephant":"The largest land animal",
                   "ocean":"A large body of saltwater",
                   "computer":"An electronic device used for computing",
                   "airplane":"A flying vehicle with wings and engines",
                   }

word,hint = random.choice(list(words_and_hints.items()))
guessed_letters = set()
attempts = 6

print("Welcome to Hangman game!")
print(f"Hint:{hint}")


def display_progress():
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display))

while attempts > 0:
    display_progress()
    guess = input("Guess a letter:").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter.")
    elif guess in word:
        guessed_letters.add(guess)
        print("Correct guess!")
        print()
    else:
        attempts -= 1
        print(f"Incorrect guess.Attempt left:{attempts}")


    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations!You've guessed the correct word:{word}")
        break
else:
        print(f"Sorry, you've run out of attempts.The word was:{word}")
