from random import randint
print('The number will be generated from 1 to your set number')
n=0

def Setup():
    while True:
        x = input('Your set number:')
        try:
            number = randint(1, int(x))
            return number, int(x)
        except ValueError or n == ' ':
            print('the input must be a number')

def Check(n, number, x):
    try:
        n = int(n)
        return True
    except ValueError or n == ' ':
        print('the input must be a number')
        guessing(number, x)
        return False

def guessing(number, x):
    your_number = input(f'Place your guess(1-{str(x)}):')
    timer = Check(your_number, number, x)
    while timer == True:
        Check(your_number, number, x)
        your_number = int(your_number)
        if your_number == number:
            print('Yay, you won')
            timer = False
            input('Press enter to exit')
        elif your_number>x or your_number<1:
            your_number = input(f'The number is between 1 to {x}:')
        else:
            if your_number>number:
                your_number = input('Try lower:')
            elif your_number<number:
                your_number = input('Try higher:')

def game():
    stopitpls = Setup()
    number = stopitpls[0]
    x = stopitpls[1]
    guessing(number, x)
    
game()

