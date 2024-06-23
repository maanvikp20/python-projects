import random

print("Welcome to HANGMAN\n")

hangman_stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

def getword():
    words = []
    with open('hangmanwords.txt', 'r') as file:
        for line in file:
            word = line.strip()  # Remove newline characters and leading/trailing whitespace
            if word:
                words.append(word)
    chosen_word = words[random.randint(0, len(words) - 1)]
    return chosen_word

def play():
    hidden_words = getword()
    word_values = []
    dashed_values = []
    guessindex = 0

    for char in hidden_words:
        if char != " ":
            dashed_values.append("_")
        else:
            dashed_values.append(" ")
            
    for char in hidden_words:
        word_values.append(char)
        
    curr_string = ''

    while word_values != dashed_values:
        guess = input("Enter a letter: ")
        if guess in word_values:
            # Reveal all instances of the guessed letter
            for index, letter in enumerate(word_values):
                if letter == guess:
                    dashed_values[index] = guess
            curr_string = ''  # Reset curr_string at the start of each iteration
            for char in dashed_values:
                curr_string += char
            print(curr_string)
            print(hangman_stages[guessindex])
            if curr_string == hidden_words:
                print("Congrats! You win!!!")
                break
        else:
            curr_string = ''  # Reset curr_string at the start of each iteration
            for char in dashed_values:
                curr_string += char
            print(curr_string)
            print("\nIncorrect!")
            guessindex += 1
            print(hangman_stages[guessindex])
            if guessindex == len(hangman_stages) - 1:
                print(f"You lose! The correct word/phrase was {hidden_words}")
                break
            
play()