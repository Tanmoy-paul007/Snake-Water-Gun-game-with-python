
import random

computer = random.choice([1,-1,0])

youchose = {"s":1,"w":-1,"g":0}
take=input("Enter your comands:- ")
you=youchose[take]

dashbord = {1:"Snake",-1:"Water",0:"Gun"}
print(f"You chose {dashbord[you]}\n computer chose {dashbord[computer]}")

if(computer==you):
    print("Match draws!")
else:
    
    # if(computer==1 and you ==-1):
    #     print("You loss tha games")
    # elif(computer==1 and you ==0):
    #     print("You win the games")
    # elif(computer==-1 and you ==1):
    #     print("You win the games")
    # elif(computer==-1 and you ==0):
    #     print("You loss tha games")
    # elif(computer== 0 and you ==1):
    #     print("You loss tha games")
    # elif(computer== 0 and you ==-1):
    #     print("You win the games")

    if ((computer-you)== -1 or (computer-you)==2):
        print("You loss the games")
    else:
        print("You win the games")

