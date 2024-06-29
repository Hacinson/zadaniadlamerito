import random

def guess_number():
    target_number = random.randint(1, 9)
    
    while True:
        guess = input("Guess a number between 1 and 9: ")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer between 1 and 9.")
            continue
        
        if guess < 1 or guess > 9:
            print("Please enter a number between 1 and 9.")
            continue
        
        if guess == target_number:
            print("Well guessed!")
            break
        else:
            print("Try again!")

guess_number()
