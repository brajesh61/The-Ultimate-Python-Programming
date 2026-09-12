import random

name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

chance = 3
count  = 0

userguess = input("Enter your guess word : ")

while count < chance:
    if(userguess == word):
        print("You Win")
        print("The word is: ", word)
        break

    elif(count >= chance and userguess != word):
        print("You Loose ! Better luck next time!")
        break

    elif(count > chance):
        print("Wrong guess! Try again")