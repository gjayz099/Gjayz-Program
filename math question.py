

#============Sample Math Questions Program================#

print("WELLCOME TO MY MATH GAME PROGRAM")
score = 0
tatal_score = 10
print("YES AND NO")
math = input("YOU WHAT TO PLAY MY GAME? : ")

if math.lower() == "yes":
    math = input("8 x 4 = ")
    if math == "32":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    math = input("8 - 4 = ")
    if math== "4":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    math = input("8 + 8 = ")
    if math == "16":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    math = input("16 + 32 = ")
    if math == "48":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    math = input("8 - 9 = ")
    if math == "1":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    math = input("8 - 8 = ")
    if math == "0":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    math = input("8 x 2 = ")
    if math == "16":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    math = input("10 + 10 = ")
    if math == "20":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    math = input("2 + 2 = ")
    if math == "4":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    math = input("6 + 10 = ")
    if math == "16":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

print("THANK U FOR USING THE PROGRAM")
print("Your score is",score*tatal_score,"%")
