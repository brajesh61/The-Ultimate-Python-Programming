import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the lower bond : "))
high = int(input("Enter upper bond : "))

print(f"You have 7 chance to guess the number between {low} to {high}. Let's start.")

correctNum = random.randint(low, high)
chance = 7
count = 0

while count < chance :
    count += 1
    userguess = int(input("Enter your guess : "))
    
    if(userguess == correctNum):
        print(f'Correct! The number is {correctNum}. You guessed it in {count} attempts.')
        break
    
    elif(count >= chance and userguess != correctNum):
        print(f"Sorry! The number was {correctNum}. Better luck next time!")

    elif(userguess < correctNum):
        print(f"Too low! Try a higher number.")
    
    elif(userguess > correctNum):
        print(f"Too high! Try a lower number.")
