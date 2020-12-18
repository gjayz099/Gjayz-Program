

#==========sample questions program==========#

print("WELLCOME MY PROGRAM")

game = input("are you play my program? yes/no ")
score = 0
total_g = 10


if game.lower() == "yes":
    game = input("what your best program language? ")
    if game.lower() == "python":
        score += 1
        print('Correct')
    else:
        print("Incorrect")

    game = input("what is the best vidoe card gtx1050/rx750? ")
    if game.lower() == "rx750":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    game = input("what is christmass day? ")
    if game.lower() == "december 25" or game.lower() == "dec 25" or game.lower() == "dec25":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    game = input("Which company popularized the term Tablet PC in 2001? ")
    if game.lower() == "microsoft":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    game = input("what is the best moba game? ")
    if game.lower() == "mobile legend" or "game.lower() == ML":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    game = input("In computer terminology, what does ROM stand for? ")
    if game.lower() == "read only memory":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    game = input("What the best gaming procesor intel/ryzen? ")
    if game.lower() == "ryzen":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    game = input("Firefox, Opera, Chrome, Safari and Explorer are types of what? ")
    if game.lower() == "web browsers" or game.lower() == "browsers":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    game = input("What the best socail media? ")
    if game.lower() == "fb" or game.lower() == "facebook":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    game = input("what is easy learn of of programing language? ")
    if game.lower() == "python":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

print("Thank U To Use Program")
print("your is SCORE",score*total_g,"%")