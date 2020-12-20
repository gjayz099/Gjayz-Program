#MY ATM MACHINE#

def menu():
    print("""=======================================================================
                            WELCOME TO GJAYZ BANK
=======================================================================""")
    money = float(input("MONEY: "))
    balance = money
    while True:
        print("""PICK YOUR TRANSACTION\n1.  DIPOSIT\n2.  WITHDRAW\n3.  BALANCE\n4.  QUIT""")
        pick = float(input("pick you transaction: "))
        if pick == 1:
            diposit = float(input("HOW MATCH YOR DIPOSIT: "))
            balance += diposit
            print("YOUR BALANACE\u20B1",balance)
            continue
        elif pick == 2:
            withdraw = float(input("how much to Withdraw (EXIT 0): "))
            if withdraw > balance:
                print("NOT ENOUGH BALANCE......\nYOUR BALANCE IS \u20B1",balance)
                continue
            elif withdraw == 0:
                print("YOUR BALANCE IS \u20B1",balance)
                quit()
            else:
                print("Your Cash is Being Counted Please Wait...")
                balance -= withdraw
                print("Balance is \u20B1",balance)
                continue
                
        elif pick == 3:
            print("YOUR BALANCE\u20B1",balance)
            continue
        elif pick == 4:
            print("THIS IS YOUR BALANCE",balance)
            quit()


#PINCODE
put = input("put your pincode: ")
while True:
    if put.lower() == "group2":
        print("sucess")
        menu()
    else:
        print("PINCODE IS WRONG")
        break

quit()