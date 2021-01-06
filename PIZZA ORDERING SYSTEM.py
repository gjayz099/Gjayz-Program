#PIZZA ORDERING SYSTEM
import os 

#MAIN PROGRAM
def main():
    print("0.EXIT\n1.BUY PIZZA\n2.ADD MENU")
    while True: 
        pick = input("pick: ")
        if pick == "0":
            print("Thankzzz")
            exit()
        elif pick == "1":
            menu()
            buy_menu()
        elif pick == "2":
            add_menu()
        else:
            print("invalid")

#ADD MENU
def add_menu():
    while True:
        pick = input("(Y To Add.....)\n(N To Exit....)\n: ")
        if pick == "n":
            main()
        if pick == "y":
            code_menu = input("NO CODE: ")
            name_menu = input("Name: ")
            price_menu = input("Price: ")
            with open('PIZZA MENU.txt',"a") as fh:
                fh.write("\n"+str(code_menu)+":"+str(name_menu)+":"+str(price_menu))
        else:
            print("invalid...")

#SEE MENU 
def menu():
    print("\n----------------------------------------\n\tWELCOME TO PIZZA HOUSE\n----------------------------------------")                    
    print("CODE            NAME              PRICE")
    print("")
    with open('PIZZA MENU.txt',"r") as menulist:
        for line in menulist:
            data = line.split(":")
            print(data[0],"\t",data[1],"\t","\u20B1{m}.00".format(m=int(data[2])))

#BUY TO MENU
def buy_menu():
    total = 0
    space = "\n"
    buy = ""
    print("")
    pick = input("PICK YOUR CODE: (X To Exit) ").upper()
    while True:
        with open('PIZZA MENU.txt',"r") as menulist:
            for line in menulist:
                data = line.split(":")
                menuCode = data[0]
                menuName = data[1]
                menuPrice = float(data[2])
                if pick == menuCode:
                    print(menuCode,"\t",menuName,"\t","\u20B1{m}.00".format(m=int(menuPrice)))
                    total += menuPrice
                    buy += space,menuName          
            pick = input("PICK YOUR CODE: (X To Exit) ").upper()

        if pick == "X":
            print("")
            print("HIRE YOUR ORDER..........\n"+str(buy))
            print("")
            print("YOUR TOTAL COST..... \u20B1"+str(total)+"0")
            exit()

main() 



    

        
                 