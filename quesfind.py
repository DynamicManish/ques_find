import random as r 
import time as t 
random_value = r.randint(2,9)

guesses = 0 #user haven't made any guess yet!
value = 0 

user_name = input('Howdy?May I know your name? ').strip().capitalize()
t.sleep(1)
print("Hello,"+"{}!".format(user_name))
t.sleep(1)
ques_choice = input('Are you ready to guess?[Y/N]:').strip()

if ques_choice == 'y':
    print('Hello,'+"{}".format(user_name))
    t.sleep(1)
    print("I am thinking of a number between 1 to 10!")
    t.sleep(1)
elif ques_choice == 'n':
    print("We're sorry, Will meet you later!")
    t.sleep(1)
    exit()
else:
    print("Wrong input!")
    t.sleep(1)
    exit()

while not (random_value == value):
    number = int(input('Enter your guess here: '))
    guesses = guesses+1
    if number == random_value:
        t.sleep(0.75)
        print("Brilliant!")
        print("You guessed it correctly,the correct number is {}".format(random_value))
        if guesses == 1:
            print("It took you {}".format(guesses)+" try in total!")
            t.sleep(1)
        else:
            print("It took you {}".format(guesses)+" tries in total!")
            t.sleep(1)

        exit()
    elif number < random_value:
        t.sleep(1)
        print("Guess higher")
    elif number > random_value:
        t.sleep(1)
        print("Guess lower")   
    else:
        t.sleep(1)
        print("Wrong inputs!")
        exit()      



