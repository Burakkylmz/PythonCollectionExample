
print("Menu")
print("--------------------")
print("For Car        --> 1")
print("For Truck      --> 2")
print("For Bus        --> 3")
print("For Motorcycle --> 4")
print("For Exit       --> 0")
print("--------------------")
while True:
    choose = int(input("Choose Your Vehicle: "))
    if (choose == 0):
        print("Program is Closing....")
        break
    elif (choose==1):
        speed = int(input("What is your speed: "))
        if (speed > 120):
            print("You punished!")
            print("Your speed is not suited to traffic rules")
        else:
            print("Your speed is suited to traffic rules.")
    elif (choose == 2):
        speed = int(input("what is your speed: "))
        if (speed > 70):
             print("You punished!")
             print("Your speed is not suited to traffic rules")
        else:
            print("Your speed is suited to traffic rules.")
    elif (choose == 3):
        speed = int(input("What is your speed: "))
        if (speed > 90):
            print("You punished!!")
            print("Your speed is not suited to traffic rules")
        else:
            print("Your speed is suited to traffic rules")
    elif (choose == 4):
        speed = int(input("What is your speed: "))
        if (speed > 100):
            print("You punished!")
            print("Your speed is not suited to traffic rules")
        else:
            print("Your speed is suited to traffic rules")