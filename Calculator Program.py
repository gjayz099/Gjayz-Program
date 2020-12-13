import math


def  Addition(num1, num2):
    return num1 + num2

def Subtraction(num1, num2):
    return num1 - num2

def Multiplication(num1, num2):
    return num1 * num2

def Division(num1, num2):
    return num1 / num2

def Modulus(num1, num2):
    return num1 % num2

def Exponent(num1, num2):
    return num1 ** num2


print("""1 Addition
2 Subtraction
3 Multiplication
4 Division
5 Mudulus
6 Exponent""")


pick = int(input("Pick your Number: "))

number_1 = float(input("Enter first number: ")) 
number_2 = float(input("Enter second number: ")) 

if pick == 1: #Addition
    print(number_1, "+", number_2, "=", Addition(number_1, number_2)) 
elif pick == 2: #Subtraction
    print(number_1, "-", number_2, "=", Subtraction(number_1, number_2)) 
elif pick == 3: #Multiplication
    print(number_1, "*", number_2, "=", Multiplication(number_1, number_2)) 
elif pick == 4: #Division
    print(number_1, "/", number_2, "=", Division(number_1, number_2)) 
elif pick == 5: #Modulus
    print(number_1, "%", number_2, "=", Modulus(number_1, number_2)) 
elif pick == 6: #Exponent
    print(number_1, "**", number_2, "=", Exponent(number_1, number_2))
else:
    print("Invalid Number")
    