import random

# Words with hints
words = {
    "python": "A popular programming language",
    "elephant": "The largest land animal",
    "guitar": "A musical instrument with strings",
    "pizza": "A popular Italian dish",
    "galaxy": "A massive system of stars and planets",
    "football": "A sport played with a round ball",
    "computer": "An electronic machine for processing data"
}

# Hangman stages (visual progress)
stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def play_game():
    word = random.choice(list(words.keys()))
    hint = words[word]
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = len(stages) - 1

    print("\n🎮 Welcome to Hangman!")
    print("Hint:", hint)

    while wrong_guesses < max_wrong:
        # Show progress
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display.strip())
        print(stages[wrong_guesses])

        # Check win
        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You guessed the word:", word)
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
            wrong_guesses += 1

    # Game over
    print(stages[wrong_guesses])
    print("💀 Game Over! The word was:", word)


# Main loop for replay
while True:
    play_game()
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("👋 Thanks for playing!")
        break