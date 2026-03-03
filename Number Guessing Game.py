import random

print("This is a Number Guessing Game\n Start The Game By Choosing difficulty \n")


attempts = 0
lvl = 'easy'

def the_num() : #random number
    numb = random.choice(range(1, 101))
    return numb

number = the_num()

def difficulty(): #Difficulty choosing sys
    diff = input("Choose Difficulty 'easy' or 'hard' :  ").lower()
    return diff
lvl = difficulty()

if lvl == 'hard':
          attempts = 5

else:
    attempts = 10

for _ in range(attempts) :
    def guess():  #Guessing System
        try:
            my_guess = int(input('guess the number btw 1 to 100:  ') )
            return my_guess
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    user_guess = guess()
    if user_guess is not None:
        if number > user_guess:
            print('Too Low')

        elif number < user_guess:
            print('Too High')


        elif user_guess == number:
            print('you win')
            attempts = -1
            break # Exit the loop if the user wins
        else:
           print('wrong')
        attempts -= 1
    else:
        continue # Skip to the next iteration if the guess was invalid

    if attempts == 0:
            print(f'you lose, the number was {number}')
            break
