import random

print("H A N G M A N")

while True:
    play_opt = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if play_opt == "exit":
        break
    elif play_opt != "play":
        continue

    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)

    letters = ['-'] * len(word)
    tries = 8

    used_letters = []
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

    guessed = False
    while tries > 0:
        print("")
        print(''.join(letters))
        letter = input("Input a letter: ")

        # Check 1 letter printed
        if len(letter) != 1:
            print("You should input a single letter")
            continue

        # Check letter is lowercase
        if letter not in lowercase_letters:
            print("It is not an ASCII lowercase letter")
            continue

        # Check if letter has already been typed
        if letter in used_letters:
            print("You already typed this letter")
            continue
        else:
            used_letters.append(letter)

        if letter in letters:
            tries = tries - 1
            print("No improvements")
        else:
            found = False
            for ci in range(len(word)):
                if word[ci] == letter:
                    found = True
                    letters[ci] = letter
            if not found:
                tries = tries - 1
                print("No such letter in the word")
        if ''.join(letters) == word:
            guessed = True
            tries = 0

    if guessed:
        print("")
        print(word)
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")

    print("")
