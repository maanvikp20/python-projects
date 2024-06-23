import random

print('Welcome to the Random Number Generator Game!!!')
while True:
    lowest = int(input("\nWhat is the lowest you want to go? "))
    highest = int(input("What is the highest you want to go? "))
    maxattempts = 3
    attempts = 0

    random_num = random.randint(lowest, highest)
    oddsofwin = 1 / (highest - lowest + 1) * 100
    while attempts != maxattempts:
        player_guess = int(input(f'\nWhat is your guess between {lowest} and {highest}\nOdds of winning: {oddsofwin}%\nGuess: '))
        
        if (player_guess < lowest or player_guess > highest) or player_guess == '':
            print('Stay within the range or put down a number!!!')
        else:
            if player_guess == random_num:
                print("Congrats! You win!")
                break
            else:
                print("Incorrect!")
                attempts += 1
    quitPlay = input('\nWould you like to stop playing (Y/N)? ')
    if quitPlay in ['Y', 'y']:
        break

print('Thank you for playing!!')