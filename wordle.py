import pickle
import secrets

with open("wordle_words.pkl", "rb") as f:
    list_of_words = pickle.load(f)

list_of_words = [item.upper() for item in list_of_words]
todays_word = (secrets.choice(list_of_words)).upper()

num_guesses = 0
guesses_allowed = 5

while num_guesses < guesses_allowed:

    guess = input("\n\nMake a guess! ").upper()
    num_guesses += 1

    if len(guess) == 5:
        if guess in list_of_words:
            print(
                f"You've guessed {guess} and it's guess number {num_guesses}.",
                end="\n\n",)
        else:
            print(f"{guess} isn't a word. Try again.", end="\n\n")
            continue
    else:
        print(f"{guess} isn't five letters. Try again.", end="\n\n")
        continue

    if guess == todays_word:
        break

    else:
        for number in range(0, len(guess), 1):
            if guess[number] == todays_word[number]:
                print(f"{guess[number]} is in the word, in the correct place.")
            elif guess[number] in list(todays_word):
                print(f"{guess[number]} is in the word, in the wrong place.")
            else:
                print(f"{guess[number]} is not in the word.")

if guess == todays_word:
    print(
        f"""
    You guessed:     {guess}
    The answer is... {todays_word}!
    Congrats! It took you {num_guesses} guesses!"""
    )

else:
    print(f"\n\nYou're out of guesses. The word was {todays_word}!")