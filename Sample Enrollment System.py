

print("\n|----------------------------|\n|WELCOME TO ENROLLMENT SYSTEM|\n|----------------------------|\n")

def again():
    while True:
        pick = input("do you want enroll another: ")
        if pick == "yes":
            data()
        elif pick == "no":
            quit()
        else:
            print("error-----------------")

def data():
    student_no = input("STUDENT NO: ")
    first_name = input("FIRST NAME: ")
    last_name = input("LAST NAME: ")
    age = input("AGE: ")
    course = input("COURSE: ")
    gender = input("GENDER: ")
    birthday = input("BIRTH DAY: ")
    yearlvl = input("YEAR LEVEL: ")
    religions = input("RELIGIONS: ")
    home_addres = input("HOME ADDRES: ")
    birth_place = input("BIRTH PLACE: ")

    order_time_stamp = "ENROLLMENT SYSTEM" + ".txt"
    with open(order_time_stamp, "a") as fh:
        fh.write("\n------------------\nSTUDENT NO# "+student_no+"\n-----------------\n")
        fh.write("FIRST NAME\t"+first_name+"\n")
        fh.write("LAST NAME\t"+last_name+"\n")
        fh.write("YOUR AGE\t"+age+"\n")
        fh.write("YOUR COURSE\t"+course+"\n")
        fh.write("GENDER   \t"+gender+"\n")
        fh.write("BIRTHDAY\t"+birthday+"\n")
        fh.write("YEAR LVL\t"+yearlvl+"\n")
        fh.write("RELIGIONS\t"+religions+"\n")
        fh.write("HOME ADDRES\t"+home_addres+"\n")
        fh.write("BIRTH PLACE\t"+birth_place+"\n")
        again()
        
while True:
    pick = input("do you want to enroll: ")
    if pick == "yes":
        data()
    elif pick == "no":
        break
    else:
        print("invalid......")

quit()