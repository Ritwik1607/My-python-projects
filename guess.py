import random
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while(random_number!=guess):
        guess=int(input(f"Enter a number between 1 and {x}\n"))
        if guess>random_number:
            print("Oops, wrong guess:( too high")
        elif guess<random_number:
            print("Oops, wrong guess:( too low")
    print("Hurrah! You guessed it right!!")
guess(10)
