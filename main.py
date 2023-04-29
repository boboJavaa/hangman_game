import random
import string

words = ["apple", "banana", "cherry", "dragonfruit", "elderberry"]
word = random.choice(words)
word_display = "_" * len(word)
wrong_guesses = []
guessed_letters = []
acceptable_input = string.ascii_lowercase
lives = 6

while True:
    print("The word:" + word_display)
    print("Wrong guesses:", "".join(wrong_guesses))
    print("Lives remaining:", lives)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Letter already used")
        continue
    elif len(guess) > 1:
        print("You can only guess one letter at a time")
        continue
    elif guess not in acceptable_input:
        print("Letter please")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_display = word_display[:i] + guess + word_display[i + 1:]
    else:
        wrong_guesses.append(guess)
        lives -= 1

    if word_display == word:
        print("Congratulations! You guessed the word:", word)
        break
    elif lives == 0:
        print("Game over. The word was:", word)
        break
