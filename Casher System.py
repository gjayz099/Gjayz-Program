inventory = {"banana": 35,
            "apple": 10,
            "orange": 20,
            "manggo": 60,
            "strubery": 100,
            "papaya": 25,
            "bayabas": 35}

print("""
Banana
Apple
Orange
Manggo
Strubery
Papaya
Bayabas
""")

Basket = []
total = []

def casher():
    user_answer = input("Hello sir/mam. what you want?""(Type 'quit' to end) : ").lower()
    while user_answer != "quit":
        if user_answer in inventory:
            Basket.append(user_answer)
            user_answer = input("yeah!! add your basket""(Type 'quit' to end) : ").lower()
        else:
            user_answer = input("I am sorry""(Type 'quit' to end) : ").lower()
casher()

print("item",Basket)
def remove():
    answer = input("Her yor item in Basket! What to remove?: ").lower()
    while answer == "yes":
        print(Basket)
        answer = input("type your item to remove :").lower()
        Basket.remove(answer)
        remove()
        
        
remove()   
  
answer = input("do you buy another? yes! or no! : ").lower()

if answer == "yes":
    casher()
    print("here is all the buy", Basket)
    for items in Basket:
        total.append(inventory[items])
    amount_to_pay = sum(total)
else:
    for items in Basket:
        total.append(inventory[items])
    amount_to_pay = sum(total)

print("your total buy.. and pay \u20B1",amount_to_pay)


