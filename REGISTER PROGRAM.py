#REGISTER SYSTEM

print("\n__________________________\nWELCOME TO REGISTER SYSTEM\n--------------------------\n")


#DATA SAVE
def save_data():
    SAVE_DATA = "YOUR DATA" + ".txt"
    with open(SAVE_DATA, "w") as fh:
        fh.write("--------------------------\n")
        fh.write("YOUR PASSWORD AND USERNAME\n")
        fh.write("--------------------------\n")
        fh.write("USERNAME: "+username)
        fh.write("\n")
        fh.write("PASSWORD: "+password)
        fh.write("\n______________\n")
        fh.write("HERE YOUR DATA")
            

#USERNAME
username = input("USERNAME: ")
#PASSWORD
password = input("PASSWORD: ")
print("")
print("YOUR FILE IS SAVE :)")
print("THANK YOU FOR USE")

save_data()