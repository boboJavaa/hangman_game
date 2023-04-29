# **Hangman Game**
This is a Python program that implements the classic game of Hangman. The player tries to guess a secret word by guessing one letter at a time. Each incorrect guess results in a part of a "hangman" being drawn on the screen. If the player runs out of guesses before guessing the word, they lose the game.

## Getting Started
1. Clone or download the repository to your local machine.
2. Install Python 3 if you don't already have it installed.
3. Open a terminal or command prompt and navigate to the directory where the program files are located.
4. Run the command python hangman.py to start the game.

## Gameplay
1. The program selects a random word from a list of words.
2. The program displays the word as a series of underscores, one for each letter in the word.
3. The player enters a letter.
4. If the letter is in the word, the program reveals the letter in the correct position(s) and prompts the player to enter another letter.
5. If the letter is not in the word, the program adds a body part to the hangman and prompts the player to enter another letter.
6. The player continues guessing letters until they guess the entire word or the hangman is complete.
7. If the player guesses the entire word, they win the game. If the hangman is complete before the word is guessed, the player loses the game.

## Features
This implementation of Hangman includes the following features:

- A list of words to choose from for each game.
- Updated showcase of the word after each guess.
- A limit of 6 incorrect guesses before the player loses the game.
- A message indicating whether the player won or lost the game.

## Contributing
If you find a bug or have a suggestion for a new feature, feel free to open an issue or submit a pull request.

