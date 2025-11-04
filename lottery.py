#lottery game
line01 = "*******************************************************"
line02 = "**********************LOTTERY**************************"
line03 = "***********************GAME****************************"

print(line01)
print(line01)
print(line01)
print(line01)
print(line01)
print(line02)
print(line03)
print(line01)
print(line01)
print(line01)
print(line01)
print(line01)

#game guideline
value = (
         """
         if the total of the three numbers is the same as the lucky number, you win $100
         Rules to play
         1. select 1st number (within 1 to 5)
         2. select 2nd number (within 1 to 5)
         3. select 3rd number (within 1 to 5)
         4. click enter and wait
         """)
print(value.upper())

#importing python libraries
import random
import math
import sys

#input your numbers
def lottery():
    while True:
        try:
            print ("")
            playerChoice1 = input(("select first number ranging from 1 to 5 >>"))
            if not playerChoice1 or playerChoice1 < '1'or playerChoice1 > '5':
                sys.exit("try again") #to detect errors in playerChoice1
            
            playerChoice2 = input(("select second number ranging from 1 to 5 >>"))
            if not playerChoice2 or playerChoice2 > '5' or playerChoice2 < '1':
                sys.exit("try again") #to detect errors in playerChoice2
            
            playerChoice3 = input(("select third number ranging from 1 to 5 >>"))
            if not playerChoice3 or playerChoice3 > '5' or playerChoice3 < '1':
                sys.exit("try again") #to detect errors in playerChoice3
            
            #to add players choices
            playerInput = int(playerChoice1) + int(playerChoice2) + int(playerChoice3)


            #for computer to pick a choice
            luckyNumber = random.randint(3,15)
            luckyNo = int(luckyNumber)

            #players and computer results
            print("")
            print("you number is " + str(playerInput) )
            print("lucky number is " + str(luckyNo) )

            #to merge result and decide the winner
            if playerInput == luckyNo:
                print ("you won $100")
            
            play_again = input("do you want to play again yes/no".lower())
            if not play_again != "yes":
                print("thanks for playing goodbye!!")
                break 
            
            
        except ValueError:
            print("enter valid number between 1 and 5")    


#start game
lottery()

    
        





