total = 0
item = []
code = []
class menu_item:  
    def __init__(self, code, name, price):
        self.code = code  
        self.name = name
        self.price = price
menu_items_list = []
menu_items_list.append( menu_item("b1", " Chicken adobo ", 60.00) ) 
menu_items_list.append( menu_item("b2", " Chicken inasal ", 80.0) ) 
menu_items_list.append( menu_item("b3", " Sinigang baboy ", 100.00) ) 
menu_items_list.append( menu_item("b4", " Pancit palabok ", 50.00) ) 
menu_items_list.append( menu_item("b5", " Pork sisig ", 60.00) ) 
menu_items_list.append( menu_item("b6", " Crispy pata ", 100.00) ) 
menu_items_list.append( menu_item("b7", " Kare-kare ", 70.00) ) 
menu_items_list.append( menu_item("b8", " Fish kinilaw ", 80.00) ) 
print("CODE     NAME        PRICE")
print("")
for obs in menu_items_list:
    print(obs.code, obs.name, obs.price, sep ="" )  

print("\n")
print("Welcome to GJAYZ Restaurant")  
print("")  
print("Please Select the item from above menu")

value = input("Please enter the item no: ")
value = str(value)

for obs in menu_items_list: 
    if value == obs.code:
        total+=obs.price
        item.append(obs.name)
        code.append(obs.code)
        print("")
        print(item)
        print("Your cart value is:")
        print("\u20B1{t}".format(t=total))
        print("\n")
                

while True:
    choice=input("Do want another order? y/n :")
    if choice == "y":
        print("\n")
        for obs in menu_items_list:
            print(obs.code, obs.name, obs.price, sep ="" )  
        print("Please Select the item from above menu")
        print("\n")
        value = input("Please enter the item no : ")
        value = str(value)
        for obs in menu_items_list: 
            if obs.code==value:
                total+=obs.price
                item.append(obs.name)
                code.append(obs.code)
                print("")
                print(item)
                print("Your cart value is:")
                print("This is your total value \u20B1{t}".format(t=total))
                print("\n")
    elif choice == "n":
        print("Your total order \u20B1{t}".format(t=total))
        while True:
            choice = input("Do You want to remove: y/n ")
            if choice == "y":
                print("Yor order Code",code)
                value = input("Please enter the item no: ")
                value = str(value)
                for obs in menu_items_list: 
                    if obs.code==value:
                        total-=obs.price
                        item.remove(obs.name)
                        code.remove(obs.code)
                        print("")
                        print(item)
                        print("Your cart value is:")
                        print("\u20B1",total)
                        print("\n")

            elif choice == "n":
                while True:
                    print("\u20B1{t} This is total total value".format(t=total))
                    money = float(input("How match your money: "))
                    if total > money:
                        print("Your money is not enough.............")
                        continue
                    elif total < money:
                        money -= total
                        print("Your change \u20B1{m}".format(m=money))
                        by = input()
                        quit()
            
quit()                  