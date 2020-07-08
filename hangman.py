import random

# Write your code here
print('H A N G M A N')

words = ['python', 'java', 'kotlin', 'javascript']

# Game loop
while True:
    # Menu and Game setup
    response = ''
    while response != 'play' and response != 'exit':
        response = input('Type "play" to play the game, "exit" to quit: > ')

    if response == 'play':
        correct_word = random.choice(words)
        correct_letters = set(correct_word)
        guessed_letters = set()
        hint = '-' * len(correct_word)
        lives = 8
    elif response == 'exit':
        break

    # Game loop
    while lives > 0:
        # Get new guess
        print('\n')
        print(hint)
        letter_guess = input('Input a letter: > ')
        
        # Error checking
        if letter_guess in guessed_letters:
            print("You already typed this letter")
            continue
        elif len(letter_guess) != 1:
            print("You should input a single letter")
            continue
        elif not letter_guess.isalpha() or not letter_guess.islower():
            print("It is not an ASCII lowercase letter")
            continue
        
        # Check if correct letter
        if letter_guess in correct_word:
            new_hint = ''
            for idx, letter in enumerate(correct_word):
                if letter == letter_guess:
                    new_hint += letter
                else:
                    new_hint += hint[idx]
            hint = new_hint
        else:
            print('No such letter in the word')
            lives -= 1
        
        guessed_letters.add(letter_guess)
        
        # Check if word has been guessed
        if hint == correct_word:
            print('\n')
            print(hint)
            print('You guessed the word!')
            print('You survived!')
            print('\n')
            break
    else:
        print('You are hanged!')
        print('\n')
