
from person import *


    
#print("",end=(" "))
if __name__ == "__main__":
    
    choice = int(input("1- Doctor\n2- Student \nEnter:"))
    if choice == 1:
        dr = Doctor("o", "o", "Osama alyhyawy")
        doctorManager = DoctorController();
        doctorManager.doctors.append(dr)
        doctorManager.login()
    elif choice == 2:
        print("I'll complete it soon")
    else:
        print('try again')
    