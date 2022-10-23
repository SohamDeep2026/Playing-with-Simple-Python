# This program takes user input of an integer between 1 and 20. Then the program will
# generate integers between 1 and 20 to guess the user input, and the randomly generated
# numbers will not be repeated. The user inputs yes/no in response. If yes is inputted,
# the program returns the number of tries it required to guess the user input. If all
# numbers are exhausted with no user input - yes, then program will return that user is lying.

from random import randint

def prog(
    random_num,
    count,
    prev_val):
    while random_num not in prev_val:
        p = ['Is', str(random_num), 'the number?']
        reply = input(' '.join(p)).lower()
        count += 1
        if reply == 'yes':
            print('Python guessed the number in', count, 'times')
            break
        else:
            prev_val.append(random_num)
            random_num = randint(1, 20)
    else:
        random_num = randint(1, 20)
        prog(random_num,
             count,
             prev_val)


num = int(input('Think a number between 1 and 20'))
random_num = randint(1, 20)
prev_val = []
count = 0
prog(random_num,
    count,
    prev_val)
