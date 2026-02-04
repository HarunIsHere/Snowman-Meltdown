import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    max_mistakes = len(STAGES) - 1
    print("\n" + "=" * 30)
    print(f"Mistakes: {mistakes}/{max_mistakes}")
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        display_word += (letter + " ") if letter in guessed_letters else "_ "

    print("Word:   ", display_word.strip())
    print("Guesses:", " ".join(guessed_letters) if guessed_letters else "-")
    print("=" * 30 + "\n")


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter ONE letter (a-z).\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        return guess


def play_one_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!\n")
        else:
            mistakes += 1
            print("Wrong guess!\n")

        # Win check
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("✅ You saved the snowman! You guessed the word:", secret_word)
            return

    # Lose
    display_game_state(mistakes, secret_word, guessed_letters)
    print("❌ The snowman melted! The secret word was:", secret_word)


def play_game():
    while True:
        play_one_game()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Goodbye!")
            break

