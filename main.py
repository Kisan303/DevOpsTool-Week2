print ("WELCOME TO SMART SERVER TEST:")
Fname= input("Enter your full-name: ")
Address =input("Enter your address: ")
Age = int(input("Enter your age: "))


if Age >= 18:
    print("Your name is: " + Fname + ", live in: " + Address + ", your age is: " + str(
            Age) + " - Valid for Smart Serve Exam")
else:
    print("Your name is: " + Fname + ", live in: " + Address + ", your age is: " + str(
    Age) + " - INVALID for Smart Serve Exam")