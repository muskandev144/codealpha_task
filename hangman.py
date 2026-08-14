
import random

words = ["python", "hangman", "coding", "computer", "programming"]

def play_hangman():
    word = random.choice(words).upper()
    attempts = 6
    guessed_letters = set()
    correct_guesses = set()
    
    print("=" * 50)
    print("WELCOME TO HANGMAN GAME!")
    print("=" * 50)
    print(f"The word has {len(word)} letters.")
    print(f"You have {attempts} attempts.\n")
    
    while attempts > 0:
        display_word = "".join([letter if letter in correct_guesses else "_" for letter in word])
        print(f"\nWord: {display_word}")
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        guess = input("\nGuess a letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            correct_guesses.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry! '{guess}' is not in the word.")
        
        if all(letter in correct_guesses for letter in word):
            print("\n" + "=" * 50)
            print("CONGRATULATIONS! You won!")
            print(f"The word was: {word}")
            print("=" * 50)
            return
    
    print("\n" + "=" * 50)
    print("GAME OVER! You ran out of attempts!")
    print(f"The word was: {word}")
    print("=" * 50)

if __name__ == "__main__":
    play_hangman()
    
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y']:
            play_hangman()
        elif play_again in ['no', 'n']:
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'")