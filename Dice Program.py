#====import Random====#
import random

#===================Virables===================#
Max = 6
Min = 1
Role_dice = "yes"

#=================While LOOP===================#
while Role_dice == "yes" or Role_dice == "y":
    print("This is You number")
    print(random.randint(Min,Max))
    print(random.randint(Min,Max))
    print("YEEEEHHHH!!!!!!")
    
#===================Imput User=================#
    Role_dice == input("Do Want TO Dice Again : ")
