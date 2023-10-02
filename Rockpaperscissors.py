import random
count=0
def play():
        global count #declaring the count variable as global
        user=input("What's your choice? 'r'for rock,'s'for scissor,'p'for paper\n") #taking input from the user
        computer=random.choice(['r','s','p'])
        if(user==computer):
            print("computer's choice:",computer)
            return "It's a tie"
        elif(user=='r'and computer=='s' or user=='p'and computer=='r' or user=='p'and computer=='s'):
            print("computer's choice:",computer)
            count=count+1
            return "You won bro!"
        print("computer's choice:",computer)
        return "you lose this time"
for i in range(1,4): #loop so that the player can have three chances
    print(play())
if(count>=2):   #final result of the game
    print(count)
    print('you are a champion!')
elif(count==1):
    print('You can still improve.')
else:
    print('you lost buddy!Better luck next time')
#This game incorporates the basics of loops and if else statements 
#Enjoy the classical game of rock,paper and scissors.
