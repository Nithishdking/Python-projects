import string #importing string to declare all type of string 
import random # importing random to randomly it can declare or assgin 

Characters = list(string.ascii_letters+"!@#$%^&*()"+string.digits)

def password_generator():
    pass_len = int(input("Give a length of a password: "))

    random.shuffle(Characters) #it shuffle the value of character
    password = []

    for x in range(pass_len):
        password.append(random.choice(Characters))

    random.shuffle(password) # it shuffle the password value

    password = "" .join(password) # i converts the list to one line string with using the empty string
    print(password)

option = input("Do you want to generate a password automatically ?  (Yes/No): ")

if option == "Yes" or "yes":
    password_generator()

elif option == "No" or"no":
    print("Thank you!")
    quit()
else:
    print("Invalid input, please enter Yes or No")
    quit()

