import random

# Hangman Art Stages
STAGES = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    """,
    """
       ------
       |    |
       |    
       |   
       |   
       |
    """,
    """
       ------
       |    
       |    
       |   
       |   
       |
    """
][::-1]

def play_game():
    words = ['PYTHON', 'DEVELOPER', 'LOGIC', 'SYSTEM', 'ALGORITHM', 'GITHUB']
    word = random.choice(words)
    word_completion = "_" * len(word)
    guessed_letters = []
    tries = 6

    print("--- HANGMAN GAME v1.0 (ZN420 Edition) ---")
    
    while tries > 0 and "_" in word_completion:
        print(STAGES[6 - tries])
        print(f"Word: {word_completion}")
        print(f"Guessed: {', '.join(guessed_letters)}")
        
        guess = input("Enter a letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print(f"You already tried '{guess}'. Stay focused! 🧠")
            continue
            
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Great! '{guess}' is in the word! ✅")
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
        else:
            tries -= 1
            print(f"Wrong! '{guess}' is not there. ❌")

    if "_" not in word_completion:
        print(STAGES[6 - tries])
        print(f"VICTORY! The word was: {word}. System hacked! 💸🚀")
    else:
        print(STAGES[6])
        print(f"GAME OVER. The word was: {word}. Try again! 💊")

if __name__ == "__main__":
    play_game()
