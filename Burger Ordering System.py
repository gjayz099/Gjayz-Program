#BURGER ORDERING SYSTEM BY GJAYZ

import time
import datetime

class Order:

    TAX_RATE = 0.09

    def __init__(self):
        self.order_dict = {
            "B1": ["\tWhopper Burger\t\t", 70, 0],
            "B2": ["\tGrill Cheeseburger\t",70, 0],
            "B3": ["\tBBQ Bacon King\t\t", 120, 0],
            "B4": ["\tBBQ Bacon King Jr\t", 90, 0],
            "B5": ["\tBacon CheeseWhopper\t", 120, 0],
            "B6": ["\tMeat Whopper Buger\t", 95, 0],
            "B7": ["\tBBQ Bacon Cheese\t", 120, 0],
            "B8": ["\tMushroom Swiss\t\t",90, 0],
            "B9": ["\tGrill Hamburger\t\t",30, 0]
        }
        self.total = 0

    #Display MENU
    def display_menu(self):
        print("Code           Name              Price")
        print("")
        for k, v in self.order_dict.items():
            print(k, v[0], "\u20B1{m}.00".format(m=v[1]))

    #GET ORDER Menu   
    def get_order(self):
        while True:
            burger_key = input("\nEnter key Code of burger to check out: ").upper()
            burger_key.strip()
            if burger_key in self.order_dict.keys():
                    try:
                        burger_num = int(input("Enter quantity: "))
                    except ValueError:
                        print("Invalid Entry!")
                        continue
                    if burger_num >= 0:
                        self.order_dict.get(burger_key)[2] += burger_num
                        break       
            else:
                print("Order Not Available!")
                continue

    #REMOVE ORDER MENU   
    def remove(self):
        while True:
            burger_key = input("\nDo you want to remove/0 To exit: ").upper()
            burger_key.strip()
            if burger_key in self.order_dict.keys():
                while True:
                    try:
                        burger_num = int(input("Enter quantity: "))
                    except ValueError:
                        print("Invalid Entry!")
                        continue
                    if burger_num >= 0:
                        self.order_dict.get(burger_key)[2] -= burger_num
                        break
                    else:
                        print("Enter Positive Integers!")
                        continue
            elif burger_key == "0":
                break

            else:
                print("Order Not Available!")
                continue 

    #SEE YOUR ITEM MENU
    def your_item(self):
        print("""\t\tTHIS IS YOUR ORDER!!!!!!\nCODE            NAME               Price         QTY""")
        for k, v in self.order_dict.items():
            if v[2] != 0:
                print(k, v[0],"\u20B1{m}".format(m="%.2f" % (v[1] * v[2])), "\t",v[2])
  
    #DISPLAY BILL NO SAVE
    def no_save_bill(self):
        time_and_date = datetime.datetime.now()
        print("                    ",time_and_date.strftime("%Y-%m-%d %I-%M-%S"))
        print("              -------BILLING STATEMENTS-------")
        for k, v in self.order_dict.items():
            if v[2] != 0:
                print(v[0], v[2],"\t\u20B1{m}".format(m="%.2f" % (v[1] * v[2])))
        for k, v in self.order_dict.items():
            self.total += v[1] * v[2]
        print("                                       ----------")
        print("\t\tTOTAL BILL","\t\t\u20B1{m}".format(m="%.2f" % self.total))
        quit()

    #DISPLAY BILL SAVE
    def save_bill(self):
        time_stamp = time.time()
        order_time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H-%M-%S")
        order_time_stamp = order_time_stamp + ".txt"
        with open(order_time_stamp, "w") as fh:
            fh.write("--------------------BILLING STATEMENTS-----------------")
            fh.write("\n")
            for k, v in self.order_dict.items():
                if v[2] != 0:
                    fh.write(v[0])
                    fh.write("\t")
                    fh.write(str(v[2]))
                    fh.write("\t")
                    fh.write("P")
                    fh.write("%.2f" % (v[1] * v[2]))
                    fh.write("\n")
            for k, v in self.order_dict.items():
                self.total += v[1] * v[2]
            fh.write("-------------------------------------------------------")
            fh.write("\n               TOTAL BILL                       P""%.2f" % self.total)
            fh.write("\n")
            fh.write("----THANK YOU FOR YOUR PATRONAGE!----")
            quit()
            
    #TRANSACTION WHILE LOOPS
    def order(self):
        print("")
        print("   WELCOME TO GJAY BURGER HOUSE ")
        while True:
            print("\nPICK TRANSACTION!!!!\n0. EXIT\n1. MUNE\n2. ORDER\n3. REMOVE\n4. SEE YOUR ORDER\n5. NO SAVE BILL and SAVE BILL") 
            TRANS = input("\nPICK YOUR TRANSACTION: ")
            print("")
            if TRANS == "1":
                self.display_menu()
            elif TRANS ==  "2":
                self.get_order()
            elif TRANS == "3":
                self.remove()
            elif TRANS == "4":
                self.your_item()
            elif TRANS == "0":
                print("THANK U......................")
                quit()
            while TRANS == "5":
                print("(NO SAVE) OR (SAVE)")
                PICK = input("\nPICK YOUR BILL TANSACTION: ").lower()
                if PICK == "no save":
                    print("")
                    self.no_save_bill()
                elif PICK == "save":
                    print("")
                    self.save_bill()
                else:
                    print("INVALID INPUT........\nTRY AGAIN........")
            else:
                print("............................")
                continue

customer = Order()
customer.order()
quit()